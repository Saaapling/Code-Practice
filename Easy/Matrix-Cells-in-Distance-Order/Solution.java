package Easy.MatrixCellsinDistanceOrder;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {

    //https://leetcode.com/problems/matrix-cells-in-distance-order/
    //Time taken: 15:45
    //Revissed BFS solution: ~30 min

    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {

        HashMap<Integer, ArrayList<int[]>> elements = new HashMap<>();

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                int distance = Math.abs(rCenter - i) + Math.abs(cCenter - j);
                if (!elements.containsKey(distance)){
                    elements.put(distance, new ArrayList<>());
                }
                elements.get(distance).add(new int[]{i,j});
            }
        }

        int[][] result = new int[rows*cols][2];
        int index = 0;
        for (Integer distance : elements.keySet()){
            for (int[] coordinate : elements.get(distance)){
                result[index] = coordinate;
                index += 1;
            }
        }

        return result;
    }


    private boolean check_coord_in_bounds(int rows, int cols, int x, int y){
        if (x >= 0 && x < rows){
            if (y >= 0 && y < cols){
                return true;
            }
        }
        return false;
    }

    public int[][] bfs_solution(int rows, int cols, int rCenter, int cCenter){
        int[][] result = new int[rows*cols][2];

        int max_dist = Math.max(rCenter, rows - rCenter) + Math.max(cCenter, cols - cCenter);

        int index = 0;
        for (int distance = 0; distance < max_dist; distance++){
            for (int i = 0; i <= distance; i++){
                int j = distance - i;
                if (check_coord_in_bounds(rows, cols, rCenter + i, cCenter + j)){
                    result[index] = new int[]{rCenter + i, cCenter + j};
                    index += 1;
                }

                if (i != 0){
                    if (check_coord_in_bounds(rows, cols, rCenter - i, cCenter + j)){
                        result[index] = new int[]{rCenter - i, cCenter + j};
                        index += 1;
                    }
                }
                if (j != 0){
                    if (check_coord_in_bounds(rows, cols, rCenter + i, cCenter - j)){
                        result[index] = new int[]{rCenter + i, cCenter - j};
                        index += 1;
                    }
                }
                if (i !=0 && j != 0){
                    if (check_coord_in_bounds(rows, cols, rCenter - i, cCenter - j)){
                        result[index] = new int[]{rCenter - i, cCenter - j};
                        index += 1;
                    }
                }
            }
        }

        return result;
    }

    public static void print_matrix(int[][] matrix){
        for (int i = 0; i < matrix.length; i++){
            System.out.println(matrix[i][0] + ", " + matrix[i][1]);
        }
    }

    public static void main(String[] args){
        Solution x = new Solution();
        int[][] result = x.bfs_solution(2,2,0,1);
        System.out.println("Results: ");
        print_matrix(result);
    }
}