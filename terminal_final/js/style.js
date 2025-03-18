"use strict";
import query from "./query.js";
import { IS_PUTER } from "./puter.js";

const style = {
    SUPPORTED_STYLES: ["default", "minimal", "standalone", "electron", "puter"],
    DEFAULT_STYLE: "default",
    apply(name) {
        const resolvedName = style.SUPPORTED_STYLES.includes(name) ? name : style.DEFAULT_STYLE;
        if (resolvedName !== "default") {
            style.apply("default");
            document.querySelectorAll(`.judge0-${resolvedName}-hidden`).forEach(e => {
                e.classList.add("judge0-style-hidden");
            });
        } else {
            style.SUPPORTED_STYLES.forEach(s => style.reverse(s));
        }

        style.SUPPORTED_STYLES.forEach(s => {
            document.querySelectorAll(`.judge0-${s}-visible`).forEach(e => {
                if (s === resolvedName) {
                    e.classList.remove("judge0-style-hidden");
                } else {
                    e.classList.add("judge0-style-hidden");
                }
            });
        });
    },
    reverse(name) {
        document.querySelectorAll(`.judge0-${name}-hidden`).forEach(e => {
            e.classList.remove("judge0-style-hidden");
        });
    }
};

export default style;

document.addEventListener("DOMContentLoaded", function () {
    if (IS_ELECTRON) {
        style.apply("electron");
    } else if (IS_PUTER) {
        style.apply("puter");
    } else {
        style.apply(query.get("style"));
    }
});
