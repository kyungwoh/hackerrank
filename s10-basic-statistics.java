// https://www.hackerrank.com/challenges/s10-basic-statistics/problem
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++) arr[i] = s.nextInt();
        s.close();
        
        int sum=0;
        for(int a : arr) sum += a;
        System.out.printf("%.1f\n",(double)sum/n);
        
        Arrays.sort(arr);
        if(n%2==0) System.out.printf("%.1f\n",(double)(arr[n/2-1]+arr[n/2])/2.0d);
        else System.out.println(arr[n/2]);
        
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int a : arr) map.merge(a,1,Integer::sum);
        
        int maxOccur=0, mode = Integer.MAX_VALUE;
        for(Map.Entry<Integer,Integer> m : map.entrySet()){
            int k = m.getKey();
            int v = m.getValue();
            if(v>maxOccur || (v==maxOccur)&&(k<mode)){
                maxOccur=v;
                mode=k;
            }
        }
        System.out.println(mode);
    }
}
