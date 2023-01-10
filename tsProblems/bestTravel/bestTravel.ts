
/**
 * The node class, represents a node within the graph
 */
class Node {
    /**
     * The value of the node
     */
    public value: number = 0;
    /**
     * Represents the edge of the node
     */
    public edges: Node[] = [];

    /**
     * One-arg constructor, which takes in a value, and sets that internal `value` 
     * 
     * @param newValue - The value we are assigning the node
     */
    public Node(newValue: number): void {
        this.value = newValue;
    }

    /**
     * 
     * @param edge - 
     */
    public add_edge(edge: Node) {
        this.edges.push(edge);
    }
}

/**
 * Computes the most optimal way to travel to n cities under the limit maxLimit
 * 
 * @param maxLimit - The summation limit, which controls the maximum distance we can travel
 * @param numberOfTowns - The minimum number of towns we can visit
 * @param distances - The list of distances we can use to contribute to the sum
 */
export function chooseBestSum(maxLimit: number, numberOfTowns: number, distances: number[]): number | null {
    let graph = 
}

console.log(chooseBestSum(163, 3, [50]));
console.log(chooseBestSum(163, 3, [50, 55, 56, 57, 58]));
console.log(chooseBestSum(230, 3, [91, 74, 73, 85, 73, 81, 87]));