using System.Text;

namespace lab_6;

public static class StringExtension
{
    public static string RemoveLatinLetters(this string input)
    {
        if (string.IsNullOrEmpty(input))
        {
            return input;
        }

        var sb = new StringBuilder();
        foreach (var c in input)
        {
            var isLatin = (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');

            if (!isLatin)
            {
                sb.Append(c);
            }
        }

        return sb.ToString();
    }
}