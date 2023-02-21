interface SafetyRegulation {
    int getMaxItemsPermitted();
}

abstract class Item implements SafetyRegulation {
    private int maxItemsPermitted;

    public void setMaxItemsPermitted(int maxItems) {
        this.maxItemsPermitted = maxItems;
    }

    public int getMaxItemsPermitted() {
        return this.maxItemsPermitted;
    }
}

class Duck extends Item {
    Duck() {
        this.setMaxItemsPermitted(5);
    }
}
class Swan extends Item {
    Swan() {
        this.setMaxItemsPermitted(2);
    }
}
class Flamingo extends Item {
    Flamingo() {
        this.setMaxItemsPermitted(3);
    }
}
class Dog extends Item {
    Dog() {
        this.setMaxItemsPermitted(20);
    }
}
class Cat extends Item {
    Cat() {
        this.setMaxItemsPermitted(20);
    }
}

public class AnimalFactory<Animal extends Item & SafetyRegulation> {

    private int unitsProduced;

    AnimalFactory() {
        this.unitsProduced = 0;
    }

    Animal continueProduction(Animal item) {
        if (unitsProduced < item.getMaxItemsPermitted()) {
            unitsProduced++;
            return item;
        }
        return null;
    }

    public int getCount() {
        return this.unitsProduced;
    }

    public static void main(String[] args) {
        // main() for testing:
        AnimalFactory<Duck> AF_D = new AnimalFactory<>();
        while(AF_D.continueProduction(new Duck()) != null);
        System.out.println("Total Ducks produced: " + AF_D.getCount());

        AnimalFactory<Swan> AF_S = new AnimalFactory<>();
        while(AF_S.continueProduction(new Swan()) != null);
        System.out.println("Total Swans produced: " + AF_S.getCount());

        AnimalFactory<Flamingo> AF_F = new AnimalFactory<>();
        while(AF_F.continueProduction(new Flamingo()) != null);
        System.out.println("Total Flamingos produced: " + AF_F.getCount());

        AnimalFactory<Dog> AF_G = new AnimalFactory<>();
        while(AF_G.continueProduction(new Dog()) != null);
        System.out.println("Total Dogs produced: " + AF_G.getCount());

        AnimalFactory<Cat> AF_C = new AnimalFactory<>();
        while(AF_C.continueProduction(new Cat()) != null);
        System.out.println("Total Cats produced: " + AF_C.getCount());

        // which produces the output
        // Total Ducks produced: 5
        // Total Swans produced: 2
        // Total Flamingos produced: 3
        // Total Dogs produced: 20
        // Total Cats produced: 20
    }
}