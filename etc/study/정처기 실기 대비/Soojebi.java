class Parent{
    public void show(){
        System.out.println("parent");
    }
}
class Child extends Parent{
    public void show(){
        System.out.println("Child");

    }
}
public class Soojebi{
    public static void main(String[] args){
        Parent pa = new Child();
        pa.show();
    }

}