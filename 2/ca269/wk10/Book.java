/**
 * class Book is parent class of PublishedBook
 * @see PublishedBook
 * @see ReadBook
 */
public class Book {
    /**
     * attributes of Book
     */
    private String title;
    private String author;
    private BookGenre genre;

    /**
     * constructor of Book
     * @param title
     * @param author
     * @param genre
     */
    Book (String title, String author, BookGenre genre) {
        setTitle(title);
        setAuthor(author);
        setBookGenre(genre);
    }

    /**
     * setter for title
     * @param title String
     */
    public void setTitle(String title) {
        this.title = title;
    }

    /**
     * setter for author
     * @param author String
     */
    public void setAuthor(String author) {
        this.author = author;
    }

    /**
     * setter for genre
     * @param genre BookGenre
     */
    public void setBookGenre(BookGenre genre) {
        this.genre = genre;
    }

    /**
     * getter for title
     * @return String
     */
    public String getTitle() {
        return this.title;
    }

    /**
     * getter for author
     * @return String
     */
    public String getAuthor() {
        return this.author;
    }

    /**
     * getter for genre
     * @return BookGenre
     */
    public BookGenre getGenre() {
        return this.genre;
    }

    /**
     * converts Book to string
     */
    public String toString() {
        return this.getTitle() + " by " + this.getAuthor();
    }
}