import { app } from "../../scripts/app.js";
import { api } from '../../scripts/api.js';

const NODE_WIDGET_MAP = {
    "JDCN_BatchImageLoadFromList": "Index",
};

class JDCNControl {
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

const ext = {
    name: "JDCN_BatchImageLoadFromList",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (NODE_WIDGET_MAP[nodeData.name]) {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated ? onNodeCreated.apply(this, []) : undefined;
                this.JDCNControl = new JDCNControl(this, NODE_WIDGET_MAP[nodeData.name]);
                this.JDCNControl.indexWidget.value = 1;
            };
        }
    },
};

app.registerExtension(ext);

api.addEventListener('jdcnse/progress', ({ detail, }) => {
    console.log(detail)
}, false);