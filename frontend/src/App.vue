<template>
  <div class="container">
    <h1>Image Annotation Tool</h1>
    <input type="file" accept=".png" @change="handleFileUpload" />
    <canvas
      ref="canvas"
      @mousedown="handleMouseDown"
      @mousemove="handleMouseMove"
      @mouseup="handleMouseUp"
    ></canvas>
    <div>
      <label for="label-input">Label:</label>
      <input type="text" id="label-input" v-model="label" />
      <button @click="saveImageSample">Save</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: null,
      canvasWidth: window.innerWidth * 0.8,
      canvasHeight: window.innerHeight * 0.8,
      label: null,
      isDrawing: false,
      startX: null,
      startY: null,
      endX: null,
      endY: null,
    };
  },
  mounted() {
    this.canvas = this.$refs.canvas;
    this.context = this.canvas.getContext("2d");
    this.canvas.width = this.canvasWidth;
    this.canvas.height = this.canvasHeight;
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.image = new Image();
        this.image.src = reader.result;
        this.image.onload = () => {
          this.context.drawImage(
            this.image,
            0,
            0,
            this.canvasWidth,
            this.canvasHeight
          );
        };
      };
      reader.readAsDataURL(file);
    },
    handleMouseDown(event) {
      this.isDrawing = true;
      const rect = this.canvas.getBoundingClientRect();
      this.startX = event.clientX - rect.left;
      this.startY = event.clientY - rect.top;
    },
    handleMouseMove(event) {
      if (!this.isDrawing) return;
      const rect = this.canvas.getBoundingClientRect();
      this.endX = event.clientX - rect.left;
      this.endY = event.clientY - rect.top;
      this.context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      this.context.drawImage(
        this.image,
        0,
        0,
        this.canvasWidth,
        this.canvasHeight
      );
      this.context.strokeRect(
        this.startX,
        this.startY,
        this.endX - this.startX,
        this.endY - this.startY
      );
    },
    handleMouseUp(event) {
      this.isDrawing = false;
    },
    saveImageSample() {
      if (this.startX > this.endX) {
        [this.startX, this.endX] = [this.endX, this.startX];
      }
      if (this.startY > this.endY) {
        [this.startY, this.endY] = [this.endY, this.startY];
      }

      const bboxX = this.startX / this.canvasWidth;
      const bboxY = this.startY / this.canvasHeight;
      const bboxWidth = (this.endX - this.startX) / this.canvasWidth;
      const bboxHeight = (this.endY - this.startY) / this.canvasHeight;
      const imageContent = this.canvas.toDataURL("image/png");
      const newImageSample = {
        image_content: imageContent,
        bbox_x: bboxX,
        bbox_y: bboxY,
        bbox_width: bboxWidth,
        bbox_height: bboxHeight,
        label: this.label,
      };

      if (this.label === null) {
        alert("Please enter a label");
        return;
      }

      if (this.image === null) {
        alert("Please upload an image");
        return;
      }

      if (this.startX === null || this.startY === null) {
        alert("Please draw a bounding box");
        return;
      }

      alert(
        "Ready to save image sample?" +
          "\n" +
          "Bbox x: " +
          newImageSample.bbox_x +
          "\n" +
          "Bbox y: " +
          newImageSample.bbox_y +
          "\n" +
          "Bbox width: " +
          newImageSample.bbox_width +
          "\n" +
          "Bbox height: " +
          newImageSample.bbox_height +
          "\n" +
          "Label: " +
          newImageSample.label +
          "\n"
      );
    },
  },
};
</script>
<style>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  font-family: Arial, sans-serif;
}

.image-uploader {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  font-family: Arial, sans-serif;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

label {
  font-size: 1.2rem;
}

input[type="text"] {
  padding: 0.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.2);
  transition: box-shadow 0.2s ease-in-out;
}

input[type="text"]:focus {
  outline: none;
  box-shadow: 0 0 0.5rem rgba(0, 0, 255, 0.5);
}

button {
  padding: 0.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.2);
  background-color: #007bff;
  color: #fff;
  transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

button:hover {
  cursor: pointer;
  background-color: #0062cc;
  box-shadow: 0 0 0.5rem rgba(0, 0, 255, 0.5);
}

canvas {
  border: 1px solid #ccc;
  border-radius: 1rem;
  box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.2);
}
</style>
