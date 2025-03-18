"use strict";

export const IS_PUTER = puter.env === "app";

export function usePuter() {
    return IS_PUTER || true;
}
