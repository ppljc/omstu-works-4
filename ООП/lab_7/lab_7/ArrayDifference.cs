namespace lab_7;

public static class ArrayDifference
{
    public static MyDel Create()
    {
        return delegate(int[] a)
        {
            if (a.Length == 0)
            {
                throw new ArgumentException();
            }
            
            var min = a[0];
            var max = a[0];

            foreach (var item in a)
            {
                if (item < min)
                    min = item;

                if (item > max)
                    max = item;
            }

            return max - min;
        };
    }
}