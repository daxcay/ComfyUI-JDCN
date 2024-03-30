import { app } from "../../scripts/app.js";

const NODE_WIDGET_MAP = {
    "JDCN_BatchImageLoadFromList": "Index",
    "JDCN_AnyFileSelector": "Index",
};

class JDCNBatchImageLoadFromListControl {
    constructor(node, widgetName) {
        this.node = node
        for (const [i, w] of this.node.widgets.entries()) {
            if (w.name === widgetName) {
                this.indexWidget = w;
            }
        }
        this.indexWidget.afterQueued = () => {
            this.indexWidget.value = this.indexWidget.value + 1
            this.indexWidget.callback(this.indexWidget.value)
        }
    }
}

const JDCN_BatchImageLoadFromList = {
    name: "JDCN_BatchImageLoadFromList",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (NODE_WIDGET_MAP[nodeData.name]) {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated ? onNodeCreated.apply(this, []) : undefined;
                this.JDCNBatchImageLoadFromListControl = new JDCNBatchImageLoadFromListControl(this, NODE_WIDGET_MAP[nodeData.name]);
                this.JDCNBatchImageLoadFromListControl.indexWidget.value = 1;
            };
        }
    },
};

class JDCNAnyFileSelectorControl {
    constructor(node, widgetName, MainController) {
        this.node = node
        for (const [i, w] of this.node.widgets.entries()) {
            if (w.name === widgetName) {
                this.indexWidget = w;
            }
            if (w.name === MainController) {
                this.controllerWidget = w;
            }
        }
        this.indexWidget.afterQueued = () => {
            let change = this.controllerWidget.value
            this.indexWidget.value = this.indexWidget.value + (1 * (change === "increment" ? 1 : change === "decrement" ? -1 : 0))
            this.indexWidget.value = this.indexWidget.value < 0 ? 0 : this.indexWidget.value
            this.indexWidget.callback(this.indexWidget.value)
        }
    }
}

const JDCN_AnyFileSelector = {
    name: "JDCN_AnyFileSelector",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (NODE_WIDGET_MAP[nodeData.name]) {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated ? onNodeCreated.apply(this, []) : undefined;
                this.JDCNAnyFileSelectorControl = new JDCNAnyFileSelectorControl(this, NODE_WIDGET_MAP[nodeData.name], "Change");
                this.JDCNAnyFileSelectorControl.indexWidget.value = 1;
            };
        }
    },
};


app.registerExtension(JDCN_BatchImageLoadFromList);
app.registerExtension(JDCN_AnyFileSelector);