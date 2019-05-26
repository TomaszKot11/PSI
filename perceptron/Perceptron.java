import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Perceptron {
    public static final int NUMBER_OF_POINTS = 30;
    public static final int NUMBER_OF_POINTS_LEARING = 30;
    public static final int NUMBER_OF_AGES = 30;

    public List<Point> points = new ArrayList<>();
    public List<Integer> t = new ArrayList<>();
    public Point weights;
    public double b;
    private Random rand = new Random();

    public static void main(String[] args) {
        Perceptron perceptron = new Perceptron();

        // inicjalizacja wag oraz bias
        perceptron.basicPerceptronInitialization();

        // uczymy perceptron na zbiorach uczacych
        perceptron.trainPerceptron();

        // testujemy perceptron
        perceptron.initPerceptron(NUMBER_OF_POINTS);
        perceptron.testPerceptron();
    }

    public void basicPerceptronInitialization() {
        weights = new Point(rand.nextDouble(), rand.nextDouble());
        b = rand.nextDouble();
    }

    // przepuszczamy przez przetestowany perceptron kazdy z punktow
    private void testPerceptron() {
        int x = 0, y = 0;
        int goodPointsCounter = 0, badPointsCounter = 0;
        for (int i = 0; i < points.size(); i++) {
            double a = weights.x + points.get(i).x + weights.y + points.get(i).y + b;

            a = a > 0 ? 1 : 0;

            if (t.get(i) != a) {
                badPointsCounter++;
            } else {
                goodPointsCounter++;
            }
        }

        System.out.println("-----Result-----");
        System.out.println("Good values: " + goodPointsCounter);
        System.out.println("Bad values: " + badPointsCounter);
        System.out.println("---------");
    }


    public void trainPerceptron() {
        boolean endAge = false;
        int tmp = NUMBER_OF_AGES;
        while (tmp-- > NUMBER_OF_AGES) {
            initPerceptron(NUMBER_OF_POINTS_LEARING);
            while (!endAge) {
                endAge = true;
                for (int i = 0; i < points.size();) {
                    // oblicz a
                    double a = weights.x * points.get(i).x + weights.y * points.get(i).y + b;
                    // oblicz y
                    a = a > 0 ? 1 : 0;

                    // oblicz wartosc bledu
                    int e = t.get(i) - (int) a;

                    if (e != 0) {
                        // zmodyfikuj wagi
                        weights.x += e * points.get(i).x;
                        weights.y += e * points.get(i).y;
                        b += e;
                        endAge = false;
                    } else {
                        i++;
                    }
                }
            }
        }
    }

    // generuje randomowy zbior punktow oraz oblicza funkcje celu
    public void initPerceptron(int numberOfPoints) {
        t.clear();
        points.clear();

        for (int i = 0; i < numberOfPoints; i++) {
            int x = rand.nextInt(40) - 20;
            int y = rand.nextInt(40) - 20;
            points.add(new Point(x, y));

            if (y <= dividingFunction(x)) {
                t.add(1);
            } else {
                t.add(0);
            }
        }
    }

    // funkcja celu - obliczanie wartosci
    private double dividingFunction(int x) {
        return 5 * x + 3;
    }
}
