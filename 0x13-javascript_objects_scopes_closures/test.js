#!/usr/bin/node
const books = [
  { title: 'The Catcher in the Rye', author: 'J.D. Salinger' },
  { title: 'To Kill a Mockingbird', author: 'Harper Lee' },
  { title: '1984', author: 'George Orwell' }
];

const transformedBooks = books.map((book, index) => {
  return {
    original: book,
    transformed: {
      title: book.title.toUpperCase(),
      author: book.author,
      index
    }
  };
});

console.log(transformedBooks);
