import java.util.ArrayList;

public class Polygon extends Shape {
    private ArrayList<Point> points;

    public Polygon(ArrayList<Point> points) {
        this.points = points;
    }

    public ArrayList<Point> getPoints() {
        return points;
    }

    public void setPoints(ArrayList<Point> points) {
        this.points = points;
    }

    // Implementing the calculateArea method for the Polygon class
    @Override
    public double calculateArea() {
        int numPoints = points.size();
        double area = 0;

        for (int i = 0; i < numPoints; i++) {
            Point currentPoint = points.get(i);
            Point nextPoint = points.get((i + 1) % numPoints);

            area += (currentPoint.getX() * nextPoint.getY()) - (nextPoint.getX() * currentPoint.getY());
        }

        return Math.abs(area) / 2;
    }

    // Implementing the calculatePerimeter method for the Polygon class
    @Override
    public double calculatePerimeter() {
        int numPoints = points.size();
        double perimeter = 0;

        for (int i = 0; i < numPoints; i++) {
            Point currentPoint = points.get(i);
            Point nextPoint = points.get((i + 1) % numPoints);

            double dx = nextPoint.getX() - currentPoint.getX();
            double dy = nextPoint.getY() - currentPoint.getY();

            perimeter += Math.sqrt(dx * dx + dy * dy);
        }

        return perimeter;
    }
}
