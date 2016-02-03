/*
 * HTree.java
 *
 * Version:
 * 1
 *
 * Revisions:
 * 2/2/15 (submitted revision)
 */
import turtle.*;

/**
 * HTree implements the java version of turtle.
 *
 * @author Colin Fausnaught (cjf1613)
 * */
public class HTree {

    /** MAX_SEGMENT_LENGTH is a constant variable which is the max length of a segment*/
    private static int MAX_SEGMENT_LENGTH = 1024;

    /**
     * init initializes a new turtle window
     *
     * @param   length      Integer, the length for the world coordinates
     * @param   depth       Integer, the depth to which the program will recurse
     * @return  t           Turtle, just a turtle Object (must be returned)
     * */
    public static Turtle init(int length, int depth){
        Turtle t = new Turtle(0,0,0);
        t.setWorldCoordinates((-length * 2), (-length * 2), (length *2), (length * 2));
        t.setCanvasTitle("H-Tree, depth: " + depth);
        return t;
    }

    /**
     * drawHTree will recursively draw the HTree.
     *
     * @param   t         Turtle, simply a turtle object to call
     * @param   length    Integer, the length of segments
     * @param   depth     Integer, the depth to recurse to
     * */
    public static void drawHTree(Turtle t, int length, int depth){
        if(depth > 0){
            t.goForward(length /2);
            t.turnLeft(90);
            t.goForward(length /2);
            t.turnRight(90);

            //Recurse
            drawHTree(t, (length / 2), (depth -1));

            //move to lower right of H
            t.turnRight(90);
            t.goForward(length);
            t.turnLeft(90);

            //recurse
            drawHTree(t, (length / 2), (depth - 1));

            //move to upper left of H
            t.turnLeft(90);
            t.goForward(length / 2);
            t.turnLeft(90);
            t.goForward(length);
            t.turnRight(90);
            t.goForward(length / 2);
            t.turnRight(90);

            //recurse
            drawHTree(t,(length / 2), (depth - 1));

            //move to lower left of H
            t.turnRight(90);
            t.goForward(length);
            t.turnLeft(90);

            //recurse
            drawHTree(t, (length / 2), (depth - 1));

            //return to center of H
            t.turnLeft(90);
            t.goForward(length / 2);
            t.turnRight(90);
            t.goForward(length / 2);


        }
    }

    /**
     * main will take command-line arguments and call the functions to draw the HTree and
     * initialize Turtle.
     *
     * @param   args        String, command-line input for the program
     * */
    public static void main(String[] args) {
        int depth = Integer.parseInt(args[0]);
        //check the depth is >= 0
        if(args.length < 2){
            System.out.println("Usage: java HTree #");
        }
        if(Integer.parseInt(args[0]) < 0){
            System.out.println("The depth must be greater than or equal to 0");
            return;
        }
        Turtle t = new Turtle(0,0,0);

        //initialize turtle
        init(MAX_SEGMENT_LENGTH, depth);


        //draw the h-tree
        drawHTree(t, MAX_SEGMENT_LENGTH, depth);

    }
} //class HTree
