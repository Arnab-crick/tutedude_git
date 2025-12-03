const express = require("express");
const path = require("path");

const app = express();

app.use(express.static(path.join(__dirname, "public")));

app.get("/todo", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "todo.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});

const payload = {
  itemId: document.getElementById("itemId").value,

  itemUuid: document.getElementById("itemUuid").value,
  itemHash: document.getElementById("itemHash").value,

  itemUuid: document.getElementById("itemUuid").value,
  itemHash: document.getElementById("itemHash").value,

  itemName: document.getElementById("itemName").value,
  itemDescription: document.getElementById("itemDescription").value,
};

