document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  const statusMsg = document.getElementById("statusMsg");
  statusMsg.innerText = "Uploading...";

  try {
    const res = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData
    });
    const data = await res.text();
    statusMsg.innerText = data;
  } catch (err) {
    statusMsg.innerText = "Upload failed 😢";
  }
});
