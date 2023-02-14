class DuckSingleton {
    private Duck duck;
    DuckSingleton(Duck duck) {
        this.duck = duck; // set the single duck at creation time
    }
    public static Duck getItem() {
        return this.duck; // always return the SAME duck
    }

    // main()
    // DuckSingleton D = new DuckSingleton(new Duck());
    // Duck d1 = getItem();
    // Duck d2 = getItem();
    // System.out.println(d1 == d2); ---> should be true
}

class Duck { }
class Swan { }

public class GenericFactory<T> {
    private T singleton;
    public T getNewItem() {
        return singleton;
    }
    GenericFactory(T singleton) {
        this.singleton = singleton;
    }

    public static void main(String[] args) {
        // creating factories: note the specifying of Ducks and Swans
        GenericFactory<Duck> DuckFactory = new GenericFactory<Duck>(new Duck());
        GenericFactory<Swan> SwanFactory = new GenericFactory<Swan>(new Swan());
        // using factories
        System.out.println(DuckFactory.getNewItem());
        System.out.println(SwanFactory.getNewItem());
    }
}