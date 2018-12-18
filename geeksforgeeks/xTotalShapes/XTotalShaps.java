package geeksforgeeks.xTotalShapes;

import java.util.*;

public class Main {

    static class Cell {
        char name;
        int row,col;
        boolean visited;

        public Cell(char name,int row, int col) {
            this.name = name;
            this.row = row;
            this.col = col;
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int testCases = Integer.parseInt(scanner.nextLine());

        for (int i = 1; i <= testCases ; i++) {
            int totalRow = scanner.nextInt();
            int totalCol = scanner.nextInt();
            scanner.nextLine();

            Cell[][] matrix = new Cell[totalRow+2][totalCol+2];
            String input = scanner.nextLine().replace(" ","");
            int index = 0;

            for (int j = 0; j < totalCol+2; j++) {
                matrix[0][j] = new Cell('0',0,j);
            }

            for (int j = 0; j < totalCol+2; j++) {
                matrix[totalRow+1][j] = new Cell('0',totalRow+1,j);
            }

            for (int j = 0; j < totalRow+2; j++) {
                matrix[j][0] = new Cell('0', j, 0);
            }

            for (int j = 0; j < totalRow+2; j++) {
                matrix[j][totalCol+1] = new Cell('0',j,totalCol+1);
            }

            for (int row = 1; row <= totalRow; row++) {
                for (int col = 1; col <= totalCol; col++) {
                    matrix[row][col] = new Cell(input.charAt(index),row,col);
                    ++index;
                }
            }

            System.out.println( getXTotalShapes(matrix,totalRow, totalCol) );
        }

    }

    static int getXTotalShapes(Cell[][] matrix, int totalRow, int totalCol) {
        int total = 0;

        for (int row = 1; row <= totalRow; row++) {
            for (int col = 1; col <= totalCol; col++) {
                if (!matrix[row][col].visited && matrix[row][col].name == 'X'){
                    ++total;
                    visit(matrix[row][col],matrix);
                }
            }
        }

        return total;
    }

    static void visit(Cell cell, Cell[][] matrix) {
        cell.visited = true;

        List<Cell> cells = getAdjacent(cell,matrix);
        for(Cell c : cells) {
            if (!c.visited && c.name=='X')
                visit(c,matrix);
        }
    }

    /*
     * diagonals not included
     */
    static List<Cell> getAdjacent(Cell cell, Cell[][] matrix) {
        List<Cell> cells = new ArrayList<>(8);

        cells.add( matrix[cell.row-1][cell.col] );
        cells.add( matrix[cell.row][cell.col-1] );
        cells.add( matrix[cell.row][cell.col+1] );
        cells.add( matrix[cell.row+1][cell.col] );

        return cells;
    }

}
