import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

// TODO: complete this object/class

public class PaginationHelper<I> {

    public ArrayList<ArrayList<I>> paginatedItems;
    public int itemsPerPage;
    public int totalPages;
    public int totalItems;

    /**
     * The constructor takes in an array of items and a integer indicating how many
     * items fit within a single page
     */
    public PaginationHelper(List<I> collection, int itemsPerPage) {
        collection.forEach(e -> System.out.println(e));
        System.out.printf("itemsperpage = %d", itemsPerPage);
        this.paginatedItems = new ArrayList<ArrayList<I>>();
        this.itemsPerPage = itemsPerPage;
        this.totalPages = (collection.size() / this.itemsPerPage) + 1;
        this.totalItems = collection.size();
        int counter = 0;
        ArrayList<I> accumulatedPage = new ArrayList<I>();
        for (final I eachItem : collection) {
            if (counter == itemsPerPage) {
                this.paginatedItems.add(accumulatedPage);
                accumulatedPage.clear();
                accumulatedPage.add(eachItem);
                counter = 1;
            } else {
                counter++;
                accumulatedPage.add(eachItem);
            }
        }
        if (accumulatedPage.size() > 0) {
            this.paginatedItems.add(accumulatedPage);
        }
    }

    /**
     * returns the number of items within the entire collection
     */
    public int itemCount() {
        return this.totalItems;
    }

    /**
     * returns the number of pages
     */
    public int pageCount() {
        return this.totalPages;
    }

    /**
     * returns the number of items on the current page. page_index is zero based.
     * this method should return -1 for pageIndex values that are out of range
     */
    public int pageItemCount(int pageIndex) {
        System.out.println("itemcount = ", pageIndex);
        return this.paginatedItems.get(pageIndex).size();
    }

    /**
     * determines what page an item is on. Zero based indexes
     * this method should return -1 for itemIndex values that are out of range
     */
    public int pageIndex(int itemIndex) {
        if (this.totalItems == 0) {
            return -1;
        }
        if (this.totalItems < (itemIndex + 1)) {
            return -1;
        }
        return (itemIndex + 1) / this.itemsPerPage;
    }

    public static void main(string[] args) {
        List<Integer> items = new ArrayList<>();
        for (int i = 1; i <= 24; i++) {
            items.add(i);
        }
        PaginationHelper<Integer> pagHelper = new PaginationHelper(items, 10);
    }
}
