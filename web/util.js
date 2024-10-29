import { app } from "../../scripts/app.js";

const NODE_WIDGET_MAP = {
    "JDCN_BatchImageLoadFromList": "Index",
    "JDCN_AnyFileSelector": "Index",
    "JDCN_AnyFileListRandom": "random_seed",
    "JDCN_BatchCounter": "Lap",
    "JDCN_BatchCounterAdvance": "Lap",
    "JDCN_StringManipulator": "index",
    "JDCN_ShowAny": "source",
};

let unAttachedControl = {}

class JDCN_BatchImageLoadFromListControl {
    constructor(node, indexWidget) {
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case indexWidget:
                    this.indexWidget = w
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

class JDCN_BatchCounterControl {
    constructor(node, seedWidget, changeWidget, rangeWidget, logWidget) {
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case seedWidget:
                    this.seedWidget = w
                    break;
                case changeWidget:
                    this.changeWidget = w
                    break;
                case rangeWidget:
                    this.rangeWidget = w
                    break;
                case logWidget:
                    this.logWidget = w
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

        this.seedWidget.beforeQueued = () => {

            let lap = this.seedWidget.value
            let range = this.rangeWidget.value
            this.logWidget.value = "" + (lap * range)

        }

    }
}

class JDCN_BatchCounterAdvanceControl {
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

class JDCN_StringManipulatorControl {
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

const JDCN_BatchCounter = {
    name: "JDCN_BatchCounter",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_BatchCounter") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_BatchCounterControl = new JDCN_BatchCounterControl(this, NODE_WIDGET_MAP[nodeData.name], "LapChange", "Range", "Log");
                this.JDCN_BatchCounterControl.seedWidget.value = 1;
            };
        }
    },
};

const JDCN_BatchCounterAdvance = {
    name: "JDCN_BatchCounterAdvance",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_BatchCounterAdvance") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_BatchCounterAdvanceControl = new JDCN_BatchCounterAdvanceControl(this, NODE_WIDGET_MAP[nodeData.name], "LapChange");
                this.JDCN_BatchCounterAdvanceControl.seedWidget.value = 1;
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

const JDCN_StringManipulator = {
    name: "JDCN_StringManipulator",
    async beforeRegisterNodeDef(nodeType, nodeData, _app) {
        if (nodeData.name === "JDCN_StringManipulator") {
            nodeType.prototype.onNodeCreated = function () {
                this.JDCN_StringManipulatorControl = new JDCN_StringManipulatorControl(this, NODE_WIDGET_MAP[nodeData.name], "index_change");
                this.JDCN_StringManipulatorControl.seedWidget.value = 1;
            };
        }
    },
};

class JDCN_ShowAnyControl {
    constructor(node, logWidget) {
        this.node = node
        for (const [i, w] of node.widgets.entries()) {
            switch (w.name) {
                case logWidget:
                    this.logWidget = w
                    break;
            }
        }
    }
}

let JDCN_ShowAny = {
    name: "JDCN_ShowAny",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "JDCN_ShowAny") {
            nodeType.prototype.onNodeCreated = function () {
                unAttachedControl["JDCN_ShowAny"] = new JDCN_ShowAnyControl(this, "text");
                unAttachedControl["JDCN_ShowAny"].node.onConnectInput = function (targetSlot, type, output, originNode, originSlot) {
                    console.log(originNode, this)
                }
                unAttachedControl["JDCN_ShowAny"].node.onSerialize = function () {
                    if (this.isOutputConnected(0)) {
                        console.log(this.getOutputNodes(0))
                    }
                }
            }
        }
        const onExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            onExecuted === null || onExecuted === void 0 ? void 0 : onExecuted.apply(this, [message]);
            console.log(this)
        };
    },
};


class JDCN_LoadImageF {

    constructor(app) {

        this.app = app
        this.nodes = []
        this.elements = {}
        this.onNodeAdded = this.onNodeAdded.bind(this);
        this.onNodeRemoved = this.onNodeRemoved.bind(this);

        this.nodeType = "JDCN_LoadImage"

    }

    onNodeAdded(node) {
        if (node.type === this.nodeType) {
            this.registerNode(node, 1)
        }
    }

    onNodeRemoved(node) {
        if (node.type === this.nodeType) {
            this.registerNode(node, 0)
        }
    }

    isValidBase64Image(base64String) {
        const base64ImageRegex = /^data:image\/[a-zA-Z0-9.+-]+;base64,[A-Za-z0-9+/]+={0,2}$/;
        return base64ImageRegex.test(base64String);
    }


    defineElements(node) {

        try {

            if (node.properties['image'] && this.isValidBase64Image(node.properties['image'])) {
                node.pasteFile(this.base64ToFile(node.properties['image'], `Image_JDCN`))
            }

            const imageWidget = node.widgets.find((w) => w.name === "image");
            if (imageWidget)
                imageWidget.afterQueued = this.afterQueued.bind(this, node)

        } catch (error) {
            console.log(error)
        }

    }

    convertImageObjectToBase64(image) {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;
        const context = canvas.getContext('2d');
        context.drawImage(image, 0, 0);
        return canvas.toDataURL();
    }

    base64ToFile(base64String, filename) {
        const arr = base64String.split(',');
        const mime = arr[0].match(/:(.*?);/)[1];
        const extension = mime.split('/')[1];
        const bstr = atob(arr[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);

        while (n--) {
            u8arr[n] = bstr.charCodeAt(n);
        }

        return new File([u8arr], `${filename}.${extension}`, { type: mime });
    }

    afterQueued(node) {
        if (node.imgs && node.imgs.length > 0) {
            let image = node.imgs[0]
            let base64 = this.convertImageObjectToBase64(image)
            node.setProperty("image", base64)
        }
    }


    registerNode(node, mode) {
        if (mode == 1) {
            if (!this.nodes.includes(node)) {
                this.nodes.push(node)
                this.defineElements(node)
            }
        }
        else if (mode == 0) {
            if (this.nodes.includes(node)) {
                this.nodes.splice(this.nodes.indexOf(node), 1)
                if (this.elements[node.id]) {
                    delete this.elements[node.id]
                }
            }
        }
    }

    registerNodes() {
        this.app.graph._nodes.forEach(node => {
            if (node.type === this.nodeType) {
                this.registerNode(node, 1)
            }
        })
    }

}

let JDCN_LoadImageFObj = new JDCN_LoadImageF(app)
let JDCN_LoadImageFExt = {
    name: "ComfyUI-JDCN_LoadImageF",
    async setup() {
        JDCN_LoadImageFObj.app.graph.onNodeAdded = JDCN_LoadImageFObj.onNodeAdded.bind(JDCN_LoadImageFObj);
        JDCN_LoadImageFObj.app.graph.onNodeRemoved = JDCN_LoadImageFObj.onNodeRemoved.bind(JDCN_LoadImageFObj);
    },
    async afterConfigureGraph() {
        console.log("ImageMatter Extension Loaded");
        JDCN_LoadImageFObj.registerNodes()
    }
};

// app.registerExtension(JDCN_BatchImageLoadFromList);
app.registerExtension(JDCN_AnyFileSelector);
app.registerExtension(JDCN_LoadImageFExt);
app.registerExtension(JDCN_AnyFileListRandom);
app.registerExtension(JDCN_BatchCounter);
app.registerExtension(JDCN_BatchCounterAdvance);
app.registerExtension(JDCN_StringManipulator);
// app.registerExtension(JDCN_ShowAny);
