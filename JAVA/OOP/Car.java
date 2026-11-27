public class Car {
    String brand;
    String color;
    
    public void display_info(){
        System.out.println("Brand: " + brand);
        System.out.println("Color: " + color);
        System.out.println("\n");
    }

    public static void main(String[] args){
        
        Car car1 = new Car();
        Car car2 = new Car();
        
        car1.brand = "Toyota";
        car1.color = "Red";
        
        car2.brand = "BMW";
        car2.color = "Black";

        car1.display_info();
        car2.display_info();

    }

}
