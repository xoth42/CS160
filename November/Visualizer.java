import java.awt.*;
import javax.swing.*;

abstract class PointShape {
    protected Point[] points;

    public PointShape(Point[] points) {
        this.points = points;
    }

    public abstract void draw(Graphics g);
}

class Line extends PointShape {
    public Line(Point[] points) {
        super(points);
    }

    @Override
    public void draw(Graphics g) {
        g.drawLine((int)points[0].getX(), (int)points[0].getY(), (int)points[1].getX(), (int)points[1].getY());
    }
}

class PointCircle extends PointShape {
    public PointCircle(Point[] points) {
        super(points);
    }

    @Override
    public void draw(Graphics g) {
        // Draw circle logic here
    }
}

public class Visualizer extends JPanel {
    private PointShape[] shapes;

    public Visualizer(PointShape[] shapes) {
        this.shapes = shapes;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (PointShape shape : shapes) {
            shape.draw(g);
        }
    }

    public static void main(String[] args) {
        Point[] linePoints = {new Point(50, 50), new Point(200, 200)};
        PointShape line = new Line(linePoints);

        PointShape[] shapes = {line};

        JFrame frame = new JFrame("Shape Visualizer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(new Visualizer(shapes));
        frame.setVisible(true);
    }
}
