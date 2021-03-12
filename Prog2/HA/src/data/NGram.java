package data;

import java.util.Arrays;

public class NGram {
    private final String[] content;
    private final String[] hist;

    public NGram(String[] contents) {
        this.content = contents;
        this.hist = new String[contents.length - 1];
        for (int i = 0; i < contents.length - 1; i++) {
            this.hist[i] = this.content[i];
        }
    }

    public String toString(){
        return Arrays.toString(this.content);
    }

    public static NGram fromString(String input) {
        String[] elems = input.trim().replaceAll("\\[", "").replaceAll("\\]", "").split(", ");
        return new NGram(elems);
    }

    public boolean equals(Object other) {
        if (!(other instanceof NGram)) {
            return false;
        }
        if (this.content.length != ((NGram) other).content.length) {
            return false;
        }

        for (int i = 0; i < this.content.length; i++) {
            if (!this.content[i].equals(((NGram) other).content[i])) {
                return false;
            }
        }
        return true;
    }

    public int hashCode() {

        int hash = 32;

        for (String s : this.content) {
            hash = 12 * hash + s.hashCode();
        }
        return hash;
    }

    public String getToken() {
        return content[content.length - 1];
    }

    public boolean checkHistory(String[] history) {
        if (this.hist.length != history.length) {
            return false;
        }
        for (int i = 0; i < this.hist.length; i++) {
            if (this.hist[i] != history[i]) {
                return false;
            }
        }
        return true;
    }

    public String[] getHistory() {
        return this.hist;
    }
    
}

