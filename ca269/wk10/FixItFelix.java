/**
 * @author kavane39
 * @see Book
 * @see PublishedBook
 * @see ReadBook
 */

/**
 * class Book is parent class of PublishedBook
 * @see PublishedBook
 * @see ReadBook
 */

class Book {
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

/**
 * class PublishedBook is parent class of ReadBook
 * class PublishedBook is child of Book
 * @see Book
 * @see ReadBook
 */
class PublishedBook extends Book{
    /**
     * attributes of PublishedBook
     * inherits title, author and genre from Book
     * aswell as associated getters and setters
     */
    private int publishedDate;
    private BookMedium medium;

    /**
     * Constructor of PublishedBook
     * @param title
     * @param author
     * @param genre
     * @param publishedDate
     * @param medium
     */
    PublishedBook (String title, String author, BookGenre genre, int publishedDate, BookMedium medium) {
        super(title, author, genre);
        setPublishedDate(publishedDate);
        setBookMedium(medium);
    }

    /**
     * setter for publishedDate
     * @param publishedDate int
     */
    public void setPublishedDate(int publishedDate) {
        this.publishedDate = publishedDate;
    }

    /**
     * setter for medium
     * @param medium BookMedium
     */
    public void setBookMedium(BookMedium medium) {
        this.medium = medium;
    }

    /**
     * getter for publishedDate
     * @return int
     */
    public int getPublishedDate() {
        return this.publishedDate;
    }

    /**
     * getter for medium
     * @return BookMedium
     */
    public BookMedium getMedium() {
        return this.medium;
    }

    /**
     * converts PublishedBook to a string
     */
    public String toString() {
        return this.getTitle() + " by " + this.getAuthor() + " (" + this.getPublishedDate() + ")";
    }
}

/**
 * class PublishedBook is child of PunlishedBook
 * @see Book
 * @see PublishedBook
 */

class ReadBook extends PublishedBook{
    /**
     * attributes of PublishedBook
     * inherits title, author, genre, publishedDate and medium from PublishedBook
     * aswell as associated getters and setters
     */
    private int readDate;
    private BookRating rating;

    /**
     * constructor for ReadBook
     * @param title
     * @param author
     * @param genre
     * @param publishedDate
     * @param readDate
     * @param medium
     * @param rating
     */
    ReadBook (String title, String author, BookGenre genre, int publishedDate, int readDate, BookMedium medium, BookRating rating) {
        super(title, author, genre, publishedDate, medium);
        setReadDate(readDate);
        setBookRating(rating);
    }

    /**
     * setter for readDate
     * @param readDate int
     */
    public void setReadDate(int readDate) {
        this.readDate = readDate;
    }

    /**
     * setter for rating
     * @param rating BookRating
     */
    public void setBookRating(BookRating rating) {
        this.rating = rating;
    }

    /**
     * getter for readdate
     * @return int
     */
    public int getReadDate() {
        return this.readDate;
    }

    /**
     * getter for rating
     * @return BookRating
     */
    public BookRating getRating() {
        return this.rating;
    }

    /**
     * converts ReadBook to a string
     */
    public String toString() {
        return this.getTitle() + " by " + this.getAuthor() + " (" + this.getPublishedDate() + ") - read in " + this.getReadDate() + ", rated " + (BookRating.valueOf("" + this.getRating()).ordinal() + 1) + "/5";
    }
}

/**
 * Test cases for FixItFelix class
 */
public class FixItFelix{
    /**
     * this function tests all 3 classes (Book, PublishedBook, ReadBook)
     * @param args[]
     */
    public static void main(String args[]) {
        Book b1 = new Book("Children of Time", "Adrian Tchaikovsky", BookGenre.Fiction);
        System.out.println(b1);
        PublishedBook b2 = new PublishedBook("The Fifth Season", "N. K. Jemesin", BookGenre.Fiction, 2015, BookMedium.AudioBook);
        System.out.println(b2);
        ReadBook b3 = new ReadBook("Perdido Street Station", "China Mieville", BookGenre.Fiction, 2000, 2020, BookMedium.EBook, BookRating.Rating5);
        System.out.println(b3);

        System.out.println(b1.getTitle());
        System.out.println(b1.getAuthor());
        System.out.println(b1.getGenre());
        System.out.println(b2.getPublishedDate());
        System.out.println(b3.getReadDate());
        System.out.println(b3.getMedium());
        System.out.println(b3.getRating());
    }
}

/**
 * enum for book mediums
 */
enum BookMedium {
    PhysicalBook,
    EBook,
    AudioBook
}

/**
 * enum for book genres
 */
enum BookGenre {
    Fiction,
    Nonfiction
}

/**
 * enum for book ratings
 */
enum BookRating {
    Rating1,
    Rating2,
    Rating3,
    Rating4,
    Rating5
}