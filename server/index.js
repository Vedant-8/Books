import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api/popular_books", async (req, res) => {
  try {
    const response = await axios.get("http://localhost:5000/api/popular_books");
    res.json(response.data);
  } catch (error) {
    res.status(500).send("Error fetching popular books");
  }
});

app.post("/api/recommend_books", async (req, res) => {
  const { user_input } = req.body;
  try {
    const response = await axios.post(
      "http://localhost:5000/api/recommend_books",
      { user_input }
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).send("Error fetching recommendations");
  }
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
