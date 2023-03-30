/**
 * @author kavane39
 * @since 2023-03-28
 * @see JarJarBinks
 * @see StarWarsCharacter
 *
 * This program reads Star Wars character data from a CSV file, creates a list of StarWarsCharacter objects,
 * and then writes the list as JSON to a new file. The program uses Apache Commons CSV library to read the CSV file
 * and Google's Gson library to write the JSON file.
*/
    import java.io.FileReader;
    import java.io.FileWriter;
    import java.io.IOException;
    import java.io.Writer;
    import java.util.ArrayList;
    import java.util.List;
    import java.io.Reader;
    import java.io.FileReader;
    import java.io.FileNotFoundException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

/**

    A class to represent a Star Wars character with various attributes such as name, height, and mass.
    */
class StarWarsCharacter {
        private String name;
        private String height;
        private String mass;
        private String hairColor;
        private String skinColor;
        private String eyeColor;
        private String birthYear;
        private String gender;
        private String homeworld;
        private String species;

    /**
        Default constructor for StarWarsCharacter.
        */
        StarWarsCharacter () { }

    /**
        Constructor for StarWarsCharacter that sets all attributes.
        @param name the character's name
        @param height the character's height
        @param mass the character's mass
        @param hair_color the character's hair color
        @param skin_color the character's skin color
        @param eye_color the character's eye color
        @param birth_year the character's birth year
        @param gender the character's gender
        @param homeworld the character's homeworld
        @param species the character's species
        */
        StarWarsCharacter(String name, String height, String mass, String hair_color, String skin_color, String eye_color, String birth_year, String gender, String homeworld, String species) {
        setName(name);
        setHeight(height);
        setMass(mass);
        setHairColor(hair_color);
        setSkinColor(skin_color);
        setEyeColor(eye_color);
        setBirthYear(birth_year);
        setGender(gender);
        setHomeworld(homeworld);
        setSpecies(species);
        }

    // setters

    /**
        Sets the character's name.
        @param name the character's name
        */
        public void setName (String name) {
        this.name = name;
        }

    /**
        Sets the character's height.
        @param height the character's height
        */
        public void setHeight (String height) {
        this.height = height;
        }

    /**
        Sets the character's mass.
        @param mass the character's mass
        */
        public void setMass (String mass) {
        this.mass = mass;
        }

    /**
        Sets the character's hair color.
        @param hair_color the character's hair color
        */
        public void setHairColor (String hair_color) {
        this.hairColor = hair_color;
        }

    /**
        Sets the character's skin color.
        @param skin_color the character's skin color
        */
        public void setSkinColor (String skin_color) {
        this.skinColor = skin_color;
        }

    /**
        Sets the character's eye color.
        @param eye_color the character's eye color
        */
        public void setEyeColor (String eye_color) {
        this.eyeColor = eye_color;
        }

    /**
        Sets the character's birth year.
        @param birth_year the character's birth year
        */
        public void setBirthYear (String birth_year) {
            this.birthYear = birth_year;
        }

    /**

    Sets the character's gender.
    @param gender the gender of the character
    */
    public void setGender(String gender) {
    this.gender = gender;
    }

/**

    Sets the character's homeworld.
    @param homeworld the homeworld of the character
    */
    public void setHomeworld(String homeworld) {
    this.homeworld = homeworld;
    }

/**

    Sets the character's species.
    @param species the species of the character
    */
    public void setSpecies(String species) {
    this.species = species;
    }

/**

    Returns the character's name.
    @return the name of the character
    */
    public String getName() {
    return this.name;
    }

/**

    Returns the character's height.
    @return the height of the character
    */
    public String getHeight() {
    return this.height;
    }

/**

    Returns the character's mass.
    @return the mass of the character
    */
    public String getMass() {
    return this.mass;
    }

/**

    Returns the character's hair color.
    @return the hair color of the character
    */
    public String getHairColor() {
    return this.hairColor;
    }

/**

    Returns the character's skin color.
    @return the skin color of the character
    */
    public String getSkinColor() {
    return this.skinColor;
    }

/**

    Returns the character's eye color.
    @return the eye color of the character
    */
    public String getEyeColor() {
    return this.eyeColor;
    }

/**

    Returns the character's birth year.
    @return the birth year of the character
    */
    public String getBirthYear() {
    return this.birthYear;
    }

/**

    Returns the character's gender.
    @return the gender of the character
    */
    public String getGender() {
    return this.gender;
    }

/**

    Returns the character's homeworld.
    @return the homeworld of the character
    */
    public String getHomeworld() {
    return this.homeworld;
    }

/**

    Returns the character's species.
    @return the species of the character
    */
    public String getSpecies() {
    return this.species;
    }

/**

    Returns a string representation of the character's information.
    @return a string with all the character's information
    */
    public String toString () {
        return "name: " + this.getName() + 
            "\nheight: " + this.getHeight() +
            "\nmass: " + this.getMass() +
            "\nhairColor: " + this.getHairColor() +
            "\nskinColor: " + this.getSkinColor() +
            "\neyeColor: " + this.getEyeColor() +
            "\nbirthYear: " + this.getBirthYear() +
            "\ngender: " + this.getGender() +
            "\nhomeworld: " + this.getHomeworld() +
            "\nspecies: " + this.getSpecies();
    }
}