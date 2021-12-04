import java.io.*;
import java.util.*;

class task2 {
    public static void main(String[] args) throws FileNotFoundException {
        int a = 0;
        int c = 0;
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<Integer> list = new ArrayList<Integer>();
        while (sc.hasNextLine())
            list.add(Integer.parseInt(sc.nextLine()));
        ArrayList<Integer> list2 = new ArrayList<Integer>();

        for (int i = 0; i < list.size() - 2; i++) {
            a = list.get(i) + list.get(i + 1) + list.get(i + 2);
            list2.add(a);
            a = 0;
        }
        System.out.println(list2);
        for (int j = 0; j < list2.size() - 1; j++) {
            if (list2.get(j + 1) > list2.get(j))
                c++;
        }
        sc.close();
        System.out.println(c);

    }

}
