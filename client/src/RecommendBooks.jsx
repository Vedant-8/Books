import React, { useState } from "react";
import axios from "axios";

const RecommendBooks = () => {
  const [userInput, setUserInput] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const handleRecommend = () => {
    axios
      .post("/api/recommend_books", { user_input: userInput })
      .then((response) => setRecommendations(response.data))
      .catch((error) =>
        console.error("Error fetching recommendations:", error)
      );
  };

  return (
    <div>
      <h1>Book Recommendations</h1>
      <input
        type="text"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Enter a book name"
      />
      <button onClick={handleRecommend}>Get Recommendations</button>
      <ul>
        {recommendations.map((book) => (
          <li key={book.book_name}>
            <img src={book.image} alt={book.book_name} />
            <p>
              {book.book_name} by {book.author}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecommendBooks;
