using System;
using System.Linq;
using System.Collections.Generic;

namespace KReverseKata;

public class LinkedListNode<T>
{
    public T Value { get; set; }
    public LinkedListNode<T> Next { get; set; }

    public LinkedListNode() { }

    public LinkedListNode(T value) : this(value, null) { }

    public LinkedListNode(T value, LinkedListNode<T> next)
    {
        Value = value;
        Next = next;
    }
}

public class Kata
{

    /// <summary>
    /// Reverses a list n of linked list nodes
    /// </summary>
    /// <param name="n">The list of linked list nodes</param>
    /// <typeparam name="T">The type that the linked list is</typeparam>
    /// <returns>The head of the reversed linked list</returns>
    public static List<LinkedListNode<T>> ReverseList<T>(List<LinkedListNode<T>> n)
    {
        List<LinkedListNode<T>> reversed = new List<LinkedListNode<T>>(n);
        reversed.Reverse();
        return reversed;
    }

    /// <summary>
    /// Takes a list of linked list nodes n, and reverses k segments of the list
    /// </summary>
    /// <param name="n">List of linked list nodes</param>
    /// <param name="k">Length of segments of n to reverse</param>
    /// <typeparam name="T">The type of linked list node</typeparam>
    /// <returns>The reversed linked list node</returns>
    public static LinkedListNode<T> KReverse<T>(LinkedListNode<T> n, int k)
    {
        List<LinkedListNode<T>> nodes = new List<LinkedListNode<T>>();
        LinkedListNode<T> tempHead = n;
        List<List<LinkedListNode<T>>> nodesList = new List<List<LinkedListNode<T>>>();
        List<LinkedListNode<T>> subSection = new List<LinkedListNode<T>>();
        while (tempHead != null)
        {
            nodes.Add(tempHead);
            tempHead = tempHead.Next;
        }

        for (int i = 0; i < nodes.Count; i++)
        {
            if (i % k == 0)
            {
                nodesList.Add(subSection.ToList());
                subSection = new List<LinkedListNode<T>>();
            }
            subSection.Add(nodes[i]);
        }

        List<LinkedListNode<T>> nodeResultantList = new List<LinkedListNode<T>>();
        for (int i = 0; i < nodesList.Count; i++)
        {
            List<LinkedListNode<T>> reversedSubsection = ReverseList(nodesList[i]);
            for (int j = 0; j < reversedSubsection.Count; j++)
            {
                nodeResultantList.Add(reversedSubsection[i]);
            }
        }
        LinkedListNode<T> newHead = nodeResultantList[0];
        if (nodeResultantList.Count > 1)
        {
            newHead.Next = nodeResultantList[1];
        }
        for (int j = 1; j < nodeResultantList.Count - 1; j++)
        {
            nodeResultantList[j].Next = nodeResultantList[j + 1];
        }
        nodeResultantList[nodeResultantList.Count - 1].Next = null;
        return newHead;
    }


    public static void Main(String[] args)
    {

        LinkedListNode<int> n = new LinkedListNode<int>();
        n.Next = new LinkedListNode<int>(2);
        n.Next.Next = new LinkedListNode<int>(3);
        n.Next.Next.Next = new LinkedListNode<int>(4);

        n = KReverse<int>(n, 2);
        while (n.Next != null)
        {
            Console.WriteLine(n.Value);
        }

    }
}