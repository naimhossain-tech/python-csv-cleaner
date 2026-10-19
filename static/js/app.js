"use strict";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(
    'form[enctype="multipart/form-data"]'
  );
  const fileInput = document.getElementById("file");

  if (!form || !fileInput) return;

  const button = form.querySelector('button[type="submit"]');
  const status = document.createElement("p");

  status.className = "file-status";
  status.setAttribute("aria-live", "polite");
  fileInput.closest("label").insertAdjacentElement("afterend", status);

  fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];

    if (!file) {
      status.textContent = "";
      status.className = "file-status";
      return;
    }

    if (!/\.(csv|xlsx)$/i.test(file.name)) {
      status.textContent = "Please select a CSV or XLSX file.";
      status.className = "file-status error";
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      status.textContent = "File is too large. Maximum size is 10 MB.";
      status.className = "file-status error";
      return;
    }

    status.textContent = "Selected: " + file.name;
    status.className = "file-status";
  });

  form.addEventListener("submit", (event) => {
    const file = fileInput.files[0];

    if (
      !file ||
      !/\.(csv|xlsx)$/i.test(file.name) ||
      file.size > 10 * 1024 * 1024
    ) {
      event.preventDefault();
      status.textContent = !file
        ? "Please select a file first."
        : "Choose a valid CSV or XLSX file up to 10 MB.";
      status.className = "file-status error";
      return;
    }

    if (button) {
      button.disabled = true;
      button.textContent = "Cleaning your data...";
    }
  });
});
