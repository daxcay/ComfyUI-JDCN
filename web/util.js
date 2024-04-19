import { app } from "../../scripts/app.js";

const NODE_WIDGET_MAP = {
    "JDCN_BatchImageLoadFromList": "Index",
    "JDCN_AnyFileSelector": "Index",
    "JDCN_AnyFileListRandom": "random_seed",
};

class JDCN_BatchImageLoadFromListControl {
    constructor(node, indexWidget) {
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case indexWidget:
                    this.indexWidget= w
                    break;
            }
        }
        this.indexWidget.afterQueued = () => {
            this.indexWidget.value = this.indexWidget.value + 1
            this.indexWidget.callback(this.indexWidget.value)
        }
    }
}

class JDCN_AnyFileSelectorControl {
    constructor(node, seedWidget, changeWidget) {
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case seedWidget:
                    this.seedWidget = w
                    break;
                case changeWidget:
                    this.changeWidget = w
                    break;
            }
        }
        this.seedWidget.afterQueued = () => {

            let change = this.changeWidget.value

            switch (change) {
                case 'increment':
                    this.seedWidget.value = this.seedWidget.value + 1
                    break;
                case 'decrement':
                    this.seedWidget.value = this.seedWidget.value - 1
                    break;
                default:
                    this.seedWidget.value = this.seedWidget.value + 0
                    break;
            }

            this.seedWidget.value = this.seedWidget.value < 0 ? 0 : this.seedWidget.value
            this.seedWidget.callback(this.seedWidget.value)

        }
    }
}

class JDCN_AnyFileListRandomControl {
    constructor(node, seedWidget, changeWidget) {
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case seedWidget:
                    this.seedWidget = w
                    break;
                case changeWidget:
                    this.changeWidget = w
                    break;
            }
        }
        this.seedWidget.afterQueued = () => {

            let change = this.changeWidget.value

            switch (change) {
                case 'increment':
                    this.seedWidget.value = this.seedWidget.value + 1
                    break;
                case 'decrement':
                    this.seedWidget.value = this.seedWidget.value - 1
                    break;
                case 'fixed':
                    this.seedWidget.value = this.seedWidget.value + 0
                    break;
                default:
                    this.seedWidget.value = Date.now()
                    break;
            }

            this.seedWidget.value = this.seedWidget.value < 0 ? 0 : this.seedWidget.value
            this.seedWidget.callback(this.seedWidget.value)

        }
    }
}


const JDCN_BatchImageLoadFromList = {
    name: "JDCN_BatchImageLoadFromList",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_BatchImageLoadFromList") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_BatchImageLoadFromListControl = new JDCN_BatchImageLoadFromListControl(this, NODE_WIDGET_MAP[nodeData.name]);
                this.JDCN_BatchImageLoadFromListControl.indexWidget.value = 1;
            };
        }
    },
};

const JDCN_AnyFileSelector = {
    name: "JDCN_AnyFileSelector",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_AnyFileSelector") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_AnyFileSelectorControl = new JDCN_AnyFileSelectorControl(this, NODE_WIDGET_MAP[nodeData.name], "Change");
                this.JDCN_AnyFileSelectorControl.seedWidget.value = 1;
            };
        }
    },
};

const JDCN_AnyFileListRandom = {
    name: "JDCN_AnyFileListRandom",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_AnyFileListRandom") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_AnyFileListRandomControl = new JDCN_AnyFileListRandomControl(this, NODE_WIDGET_MAP[nodeData.name], "seed_change");
                this.JDCN_AnyFileListRandomControl.seedWidget.value = Date.now()
            };
        }
    },
};

// app.registerExtension(JDCN_BatchImageLoadFromList);
app.registerExtension(JDCN_AnyFileSelector);
app.registerExtension(JDCN_AnyFileListRandom);