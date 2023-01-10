/**
 * Whether or not the card can be played
 * 
 * @param {string} resources - Your current resources
 * @param {string} required - The resources required 
 */
const canPlay = (resources, required) => {
    /**
     * @type {Map}
     */
    const requiredLetters = new Map();
    for (let i = 0; i < required.length; i++) {
        if (requiredLetters.has(required.charAt(i))) {
            requiredLetters.set(required.charAt(i), requiredLetters.get(required.charAt(i)) + 1);
        } else {
            requiredLetters.set(required.charAt(i), 1);
        }
    }
    const resourcesLetters = new Map();
    for (let i = 0; i < resources.length; i++) {
        if (resourcesLetters.has(resources.charAt(i))) {
            resourcesLetters.set(resources.charAt(i), resourcesLetters.get(resources.charAt(i)) + 1);
        } else {
            resourcesLetters.set(resources.charAt(i), 1);
        }
    }
    return [...resourcesLetters.keys()].every(e => requiredLetters.has(e) && resourcesLetters.get(e) >= requiredLetters.get(e));
}

/**
 * Makes the play on the card, given the resources and playIn and playOut values
 * 
 * @param {string} resources - Your current resources
 * @param {string} playIn - The resources you are losing
 * @param {string} playOut - The resources you are gaining
 */
const makePlay = (resources, playIn, playOut) => {
    
}

class GraphNodeEdge {
    /**
     * @type {GraphNode}
     */
    connected_node;
    /**
     * @type {GraphNode}
     */
    target_node;
    /**
     * @type {string}
     */
    weight;
}

class GraphNode {
    /**
     * @type {Array<GraphNodeEdge>}
     */
    edges;

    /**
     * Adds a node to the list of connected nodes this current node contains
     * 
     * @param {GraphNode} new_node - The node we are adding 
     */
    add_edge(new_node) {
        this.edges.push({ connected_node: this, target_node: new_node, weight: })
    }


}

class Graph {
    root;

}

const findCombo = function(starting, cards) {
    // create a graph, of all potential plays the user can make from resources I, and then assign a weight to each edge, see if there is any vertex that contains the resource D, and if there is, follow
    // the path back and see if it's possible to reach the beginning of the path from the end.
    // root being the initial resources
    
    return {
        preparation: [],
        loop: []
    }
}