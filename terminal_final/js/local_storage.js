"use strict";
const ls = {
    set(key, value) {
        try {
            if (value == null) {
                ls.del(key);
                return;
            }

            if (typeof value === "object") {
                value = JSON.stringify(value);
            }

            localStorage.setItem(key, value);
        } catch (ignorable) {
        }
    },
    get(key) {
        try {
            const value = localStorage.getItem(key);
            try {
                return JSON.parse(value);
            } catch (ignorable) {
                return value;
            }
        } catch (ignorable) {
            return null;
        }
    },
    del(key) {
        try {
            localStorage.removeItem(key);
        } catch (ignorable) {
        }
    }
};

export default ls;
