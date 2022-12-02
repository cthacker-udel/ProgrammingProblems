/**
 *
 * @param {number[]} arr
 */
function multCurry(arr) {
  return (mult) => arr.map((eachNumber) => eachNumber * mult);
}

/**
 *
 * @param {number[]} arr
 */
function mirror(arr) {
  return arr.concat(arr.slice().reverse());
}

class Book {
  title;
  author;

  constructor(title, author) {
    this.title = title;
    this.author = author;
  }

  getTitle() {
    return `Title: ${this.title}`;
  }

  getAuthor() {
    return `Author: ${this.author}`;
  }
}

const PP = new Book("Pride and Prejudice", "Jane Austen");
const H = new Book("Hamlet", "William Shakespeare");
const WP = new Book("War and Peace", "Leo Tolstoy");
