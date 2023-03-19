import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.NoSuchFieldException;
import java.lang.NoSuchMethodException;

public class Reflection {
    @SuppressWarnings("unchecked")
    public static boolean checkField(Class cls, String str) {
        if (cls == null) { return false; }
        try {
            Field field = cls.getField(str);
            return true;
        } catch(NoSuchFieldException e) {}
        try {
            Field field = cls.getSuperclass().getField(str);
            return true;
        } catch(NoSuchFieldException e) {}
        return false;
    }

    @SuppressWarnings("unchecked")
    public static boolean checkMethod(Class cls, String str) {
        if (cls == null) { return false; }
        try {
            Method method = cls.getDeclaredMethod(str);
            return true;
        } catch(NoSuchMethodException e) {}
        try {
            Method method = cls.getSuperclass().getDeclaredMethod(str);
            return true;
        } catch(NoSuchMethodException e) {}
        return false;
    }

    @SuppressWarnings("unchecked")
    public static boolean isClass(Class cls) {
        return cls instanceof Class && !cls.isInterface();
    }

    @SuppressWarnings("unchecked")
    public static boolean isInterface(Class cls) {
        return cls.isInterface();
    }

    @SuppressWarnings("unchecked")
    public static boolean hasAncestor(Class cls, String str) {
        if (cls == null) { return false; }
        Class par = cls.getSuperclass();
        if (par == null) { return false; }
        while (!par.equals(Object.class)) {
            if (par.getName().equals(str)) {
                return true;
            }
            par = par.getSuperclass();
        }
        for (Class parInter : cls.getInterfaces()) {
            if (parInter.getName().equals(str)) { return true; }
        }
        return false;
    }

    public String WishYouA() {
        return "Happy St. Patrick's Day!";
    }

    public static void main(String args[]) {
        System.out.println("checkField(C.class, 'f_A'): " + Reflection.checkField(C.class, "f_A"));
        System.out.println("checkMethod(C.class, 'm_X'): " + Reflection.checkMethod(C.class, "m_X"));
        System.out.println("isClass(C.class): " + Reflection.isClass(C.class));
        System.out.println("isClass(X.class): " + Reflection.isClass(X.class));
        System.out.println("isInterface(C.class): " + Reflection.isInterface(C.class));
        System.out.println("isInterface(X.class): " + Reflection.isInterface(X.class));
        System.out.println("hasAncestor(C.class, 'A'): " + Reflection.hasAncestor(C.class, "A"));
        System.out.println("hasAncestor(C.class, 'C'): " + Reflection.hasAncestor(C.class, "C"));
        System.out.println("hasAncestor(C.class, 'X'): " + Reflection.hasAncestor(C.class, "X"));
        System.out.println("hasAncestor(B.class, 'X'): " + Reflection.hasAncestor(B.class, "X"));
        System.out.println("hasAncestor(X.class, 'X'): " + Reflection.hasAncestor(X.class, "X"));
    }
}

class A {
    public String f_A;
}

class B extends A { }

interface X {
    void m_X();
}

class C extends B implements X {
    private String f_C;
    public void m_X() { }
}
