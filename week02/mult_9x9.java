public class mult_9x9 {
    public static void main(String[] args) {

        for (int i = 1; i <= 9; i++) {        // 外層：控制列
            for (int j = 1; j <= 9; j++) {    // 內層：控制行
                System.out.printf("%dx%d=%2d\t", i, j, i * j);
            }
            System.out.println();  // 每列結束換行
        }

    }
}