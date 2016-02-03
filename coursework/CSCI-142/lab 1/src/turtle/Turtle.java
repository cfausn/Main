/*************************************************************************
 *  Compilation:  javac Turtle.java
 *  Execution:    java Turtle
 *
 *  Data type for turtle graphics using standard draw.
 *  
 *  Copyright 2007, Robert Sedgewick and Kevin Wayne. 
 *  
 *  Version:
 *  	$Id$
 *  
 *  Revisions:
 *  	$Log$
 *
 *************************************************************************/

package turtle;
import java.awt.Color;

/**
 * A turtle graphics library built on StdDraw.
 * 
 * @author Robert Sedgewick, Kevin Wayne
 */
public class Turtle {
    private double x, y;     // turtle is at (x, y)
    private double angle;    // facing this many degrees counterclockwise from the x-axis

    /**
     * Construct the Turtle object.
     * 
     * @param x0 The starting x-coordinate for the turtle.
     * @param y0 The starting y-coordinate for the turtle.
     * @param a0 The degrees facing counterclockwise from the x-axis
     */
    public Turtle(double x0, double y0, double a0) {
        x = x0;
        y = y0;
        angle = a0;
    }
    
    /**
     * Set the user-defined coordinate system.
     * 
     * @param x0 The x-coordinate of the lower left corner of canvas.
     * @param y0 The y-coordinate of the lower left corner of canvas.
     * @param x1 The x-coordinate of the upper right corner of canvas.
     * @param y1 The y-coordinate of the upper right corner of canvas.
     */
    public void setWorldCoordinates(double x0, double y0, double x1, double y1) {
    	StdDraw.setXscale(x0, x1);
    	StdDraw.setYscale(y0, y1);
    }

    /**
     * Turn the turtle left.
     * 
     * @param delta The rotate orientation delta in degrees counterclockwise.
     */
    public void turnLeft(double delta) {
        angle += delta;
    }
    
    /**
     * Turn the turtle right.
     * 
     * @param delta The rotate orientation delta in degrees clockwise.
     */    
    public void turnRight(double delta) {
        angle -= delta;
    }

    /**
     * Move the turtle forward.
     * 
     * @param step The amount to move forward with the pen down.
     */
    public void goForward(double step) {
        double oldx = x;
        double oldy = y;
        x += step * Math.cos(Math.toRadians(angle));
        y += step * Math.sin(Math.toRadians(angle));
        StdDraw.line(oldx, oldy, x, y);
    }

    /**
     * Pause the turtle from drawing.
     * 
     * @param t The amount in milliseconds to pause the turtle.
     */
    public void pause(int t) {
        StdDraw.show(t);
    }

    /**
     * Set the turtle's pen color.
     * 
     * @param color The pen color.
     */
    public void setPenColor(Color color) {
        StdDraw.setPenColor(color);
    }

    /**
     * Set the thickness of the turtle's pen.
     * 
     * @param radius The dot thickness.
     */
    public void setPenRadius(double radius) {
        StdDraw.setPenRadius(radius);
    }

    /**
     * Set the canvas size.
     * 
     * @param width The canvas width.
     * @param height The canvas height.
     */
    public void setCanvasSize(int width, int height) {
        StdDraw.setCanvasSize(width, height);
    }
    
    /**
     * Set the canvas title.
     * 
     * @param title The canvas title.
     */
    public void setCanvasTitle(String title) {
    	StdDraw.setTitle(title);
    }

    // sample client for testing
    public static void main(String[] args) {
        double x0 = 0.5;
        double y0 = 0.0;
        double a0 = 60.0;
        double step = Math.sqrt(3)/2;
        Turtle turtle  = new Turtle(x0, y0, a0);
        turtle.goForward(step);
        turtle.turnLeft(120.0);
        turtle.goForward(step);
        turtle.turnLeft(120.0);
        turtle.goForward(step);
        turtle.turnLeft(120.0);
    }
}
