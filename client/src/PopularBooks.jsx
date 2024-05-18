import React, { useState, useEffect } from "react";
import axios from "axios";

const PopularBooks = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios
      .get("/api/popular_books")
      .then((response) => setBooks(response.data))
      .catch((error) => console.error("Error fetching popular books:", error));
  }, []);

  return (
    <div>
      <h1>Popular Books</h1>
      <ul>
        {books.map((book) => (
          <li key={book.book_name}>
            <img src={book.image} alt={book.book_name} />
            <p>
              {book.book_name} by {book.author}
            </p>
            <p>
              Votes: {book.votes}, Rating: {book.rating}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PopularBooks;
