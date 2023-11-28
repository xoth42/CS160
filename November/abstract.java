import java.util.ArrayList;

// Abstract class for defining basic shapes
abstract class Shape {
    // Abstract method to calculate the area of the shape
    public abstract double calculateArea();

    // Abstract method to calculate the perimeter of the shape
    public abstract double calculatePerimeter();
}

// Circle class that extends the Shape class
class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    // Implementing the calculateArea method for the Circle class
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    // Implementing the calculatePerimeter method for the Circle class
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
}

// Rectangle class that extends the Shape class
class Rectangle extends Shape {
    private double length;
    private double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    @Override
    public double calculatePerimeter() {
        return 2 * (length + width);
    }

    // Implementing the calculateArea method for the Rectangle class
    @Override
    public double calculateArea() {
        return length * width;
    }

    // Polygon class that extends the Shape class
    
}
