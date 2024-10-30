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

class Store {
    constructor(storeName) {
        this.dbName = 'JDCN';
        this.storeName = storeName || 'LoadImage';
        this.dbVersion = 1;
        this.db = null;
        this.isIndexedDBAvailable = 'indexedDB' in window;
    }

    openDB() {
        return new Promise((resolve, reject) => {
            if (!this.isIndexedDBAvailable) {
                resolve(null);
                return;
            }

            if (this.db) {
                resolve(this.db);
                return;
            }

            const request = indexedDB.open(this.dbName, this.dbVersion);

            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains(this.storeName)) {
                    db.createObjectStore(this.storeName);
                }
            };

            request.onsuccess = (event) => {
                this.db = event.target.result;
                resolve(this.db);
            };

            request.onerror = (event) => {
                console.error('IndexedDB error:', event.target.errorCode);
                resolve(null);
            };
        });
    }

    /**
     * Stores a value under a key.
     * @param {string} key - The key to store the value under.
     * @param {*} value - The value to store (can be an object).
     * @returns {Promise<void>}
     */
    set(key, value) {
        if (this.isIndexedDBAvailable) {
            return this.openDB().then((db) => {
                if (db) {
                    return new Promise((resolve, reject) => {
                        const transaction = db.transaction([this.storeName], 'readwrite');
                        const store = transaction.objectStore(this.storeName);
                        const request = store.put(value, key);

                        request.onsuccess = () => {
                            resolve();
                        };

                        request.onerror = (event) => {
                            console.error('IndexedDB set error:', event.target.errorCode);
                            reject(event.target.errorCode);
                        };
                    });
                } else {
                    try {
                        localStorage.setItem(key, JSON.stringify(value));
                        return Promise.resolve();
                    } catch (e) {
                        return Promise.reject(e);
                    }
                }
            });
        } else {
            try {
                localStorage.setItem(key, JSON.stringify(value));
                return Promise.resolve();
            } catch (e) {
                return Promise.reject(e);
            }
        }
    }

    /**
     * Retrieves a value by key.
     * @param {string} key - The key of the value to retrieve.
     * @returns {Promise<*>} - The stored value or null if not found.
     */
    get(key) {
        if (this.isIndexedDBAvailable) {
            return this.openDB().then((db) => {
                if (db) {
                    return new Promise((resolve, reject) => {
                        const transaction = db.transaction([this.storeName], 'readonly');
                        const store = transaction.objectStore(this.storeName);
                        const request = store.get(key);

                        request.onsuccess = (event) => {
                            const data = event.target.result;
                            resolve(data);
                        };

                        request.onerror = (event) => {
                            console.error('IndexedDB get error:', event.target.errorCode);
                            reject(event.target.errorCode);
                        };
                    });
                } else {
                    const item = localStorage.getItem(key);
                    const data = item ? JSON.parse(item) : null;
                    return Promise.resolve(data);
                }
            });
        } else {
            const item = localStorage.getItem(key);
            const data = item ? JSON.parse(item) : null;
            return Promise.resolve(data);
        }
    }

    /**
     * Deletes a value by key.
     * @param {string} key - The key of the value to delete.
     * @returns {Promise<void>}
     */
    remove(key) {
        if (this.isIndexedDBAvailable) {
            return this.openDB().then((db) => {
                if (db) {
                    return new Promise((resolve, reject) => {
                        const transaction = db.transaction([this.storeName], 'readwrite');
                        const store = transaction.objectStore(this.storeName);
                        const request = store.delete(key);

                        request.onsuccess = () => {
                            resolve();
                        };

                        request.onerror = (event) => {
                            console.error('IndexedDB remove error:', event.target.errorCode);
                            reject(event.target.errorCode);
                        };
                    });
                } else {
                    localStorage.removeItem(key);
                    return Promise.resolve();
                }
            });
        } else {
            localStorage.removeItem(key);
            return Promise.resolve();
        }
    }
}

class JDCN_LoadImageF {

    constructor(app) {
        this.app = app;
        this.nodes = [];
        this.onNodeAdded = this.onNodeAdded.bind(this);
        this.onNodeRemoved = this.onNodeRemoved.bind(this);
        this.nodeType = "JDCN_LoadImage";
        this.store = new Store();
        this.workflow_name = ''; // Initialize workflow_name

        this.dialogObserver = null; // To keep reference to the observer
        this.dialogElement = null;  // To keep reference to the dialog element
        this.inputElement = null;   // To keep reference to the input element
        this.buttonElement = null;  // To keep reference to the button element

        this.images = {}

        this.attachDialog()
        this.setupJDCNFileInput()
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

    async postImage(id, base64) {
        try {
            await this.store.set(id, base64)
            console.log('Image saved:', id);
        } catch (error) {
            console.error('Error saving image:', error);
        }
    }

    async getImage(id) {
        try {
            let base64 = await this.store.get(id)
            if (base64) {
                return base64;
            }
            else {
                return null
            }
        } catch (error) {
            console.error('Error retrieving image:', error);
            return null;
        }
    }

    async isImagePresentOnServer(name) {

        const url = `/api/view?filename=${name}&type=input&subfolder=`;
        try {
            const response = await fetch(url, { method: 'HEAD', cache: 'no-cache' });
            return response.status !== 404;
        } catch (error) {
            console.error("Error checking image presence:", error);
            return false;
        }

    }

    async defineElements(node) {
        try {
            if (node.properties['image']) {
                let name = node.properties['image']
                let base64 = await this.getImage(name)
                if (base64) {
                    this.images[name] = base64
                    let onServer = await this.isImagePresentOnServer(name)
                    if (!onServer) {
                        node.pasteFile(this.base64ToFile(base64, name))
                    }
                }
            }
            const imageWidget = node.widgets.find((w) => w.name === "image");
            if (imageWidget) {
                imageWidget.afterQueued = this.afterQueued.bind(this, node)
            }
        } catch (error) {
            console.log(error)
        }
    }

    clearDefinedElemnts(node) {

        try {
            if (node.properties['image']) {
                let name = node.properties['image']
                delete this.images[name]
            }
            const imageWidget = node.widgets.find((w) => w.name === "image");
            if (imageWidget) {
                imageWidget.afterQueued = null
            }

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
        const bstr = atob(arr[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);

        while (n--) {
            u8arr[n] = bstr.charCodeAt(n);
        }

        return new File([u8arr], filename, { type: mime });
    }

    async afterQueued(node) {
        try {
            if (node.imgs && node.imgs.length > 0) {
                const save_in_export = node.widgets.find(w => w.name === "save_in_export");
                if (save_in_export && save_in_export.value) {
                    let name = node.widgets[0].value || node.widgets[0]._real_value
                    let image = node.imgs[0]
                    let base64 = this.convertImageObjectToBase64(image)
                    console.log("Trying:", name)
                    node.setProperty("image", name)
                    this.images[name] = base64
                    await this.postImage(name, base64)
                }
            }
        } catch (error) {
            console.log(error)
        }

    }

    async collectImage(node) {
        try {
            if (node.imgs && node.imgs.length > 0) {
                let name = node.widgets[0].value || node.widgets[0]._real_value
                console.log(node.widgets[0].value, node.widgets[0]._real_value)
                let image = node.imgs[0]
                let base64 = this.convertImageObjectToBase64(image)
                console.log("Trying:", name)
                node.setProperty("image", name)
                this.images[name] = base64
            }
        } catch (error) {
            console.log(error)
        }

    }

    registerNode(node, mode) {
        if (mode == 1) {
            if (!this.nodes.includes(node)) {
                this.nodes.push(node)
                this.defineElements(node)
            }
            else {
                if (this.nodes.includes(node)) {
                    this.clearDefinedElemnts(node)
                    this.nodes.splice(this.nodes.indexOf(node), 1)
                }
                if (!this.nodes.includes(node)) {
                    this.nodes.push(node)
                    this.defineElements(node)
                }
            }
        }
        else if (mode == 0) {
            if (this.nodes.includes(node)) {
                this.nodes.splice(this.nodes.indexOf(node), 1)
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

    attachDialog() {

        if (this.dialogObserver) {
            this.dialogObserver.disconnect();
        }

        this.dialogObserver = new MutationObserver((mutationsList) => {
            for (let mutation of mutationsList) {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach((node) => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            this.checkAndAttachToDialog(node);
                        }
                    });
                    mutation.removedNodes.forEach((node) => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            this.checkAndDetachFromDialog(node);
                        }
                    });
                }
            }
        });

        this.dialogObserver.observe(document.body, { childList: true, subtree: true });

    }

    checkAndAttachToDialog(node) {
        if (node) {
            const dialogNode = node.querySelector('h3');
            if (dialogNode && dialogNode.textContent == "Export Workflow") {
                this.attachEventsToDialog(node);
            }
        }
    }

    attachEventsToDialog(dialogNode) {
        this.dialogElement = dialogNode;
        this.inputElement = dialogNode.querySelector('[data-pc-name="inputtext"]');
        this.buttonElement = dialogNode.querySelector('[data-pc-name="button"]');
        if (this.inputElement) {
            this.workflow_name = this.inputElement.value;
            this.inputElement.addEventListener('input', this.onInputChange);
        }
        if (this.buttonElement) {
            this.buttonElement.addEventListener('click', this.onButtonClick);
        }
    }

    onInputChange = (event) => {
        this.workflow_name = event.target.value;
    };

    onButtonClick = () => {
        this.saveAsJDCN()
    };

    checkAndDetachFromDialog(node) {
        if (node === this.dialogElement) {
            this.detachEventsFromDialog();
        } else if (node.contains(this.dialogElement)) {
            this.detachEventsFromDialog();
        }
    }

    detachEventsFromDialog() {
        if (this.inputElement) {
            this.inputElement.removeEventListener('input', this.onInputChange);
            this.inputElement = null;
        }
        if (this.buttonElement) {
            this.buttonElement.removeEventListener('click', this.onButtonClick);
            this.buttonElement = null;
        }
        this.dialogElement = null;
    }

    async forJD() {
        this.images = {}
        let nodes = 0;
        for (const node of this.nodes) {
            const save_in_export = node.widgets.find(w => w.name === "save_in_export");
            if (save_in_export && save_in_export.value) {
                await this.collectImage(node);
                nodes++;
            }
        }
        return nodes;
    }

    setupJDCNFileInput() {

        document.body.addEventListener('dragover', (event) => {
            event.preventDefault();
        });

        document.body.addEventListener('drop', (event) => {
            event.preventDefault();
            const file = event.dataTransfer.files[0];
            if (file && file.name.endsWith('.json')) {
                handleJDCNFile(file);
            }
        });

        let obj = this

        async function handleJDCNFile(file) {
            const reader = new FileReader();
            reader.onload = async (e) => {
                try {
                    let graph = JSON.parse(e.target.result);
                    let images = { ...graph.workflow_images }; // Clone to avoid mutating original object
                    delete graph.workflow_images;

                    for (const name in images) {
                        if (images.hasOwnProperty(name) && obj.isValidBase64Image(images[name])) {
                            await obj.postImage(name, images[name]);
                        }
                    }

                    obj.registerNodes()

                } catch (error) {
                    console.error("Error parsing .json file:", error);
                }
            };
            reader.readAsText(file);
        }
    }

    async saveAsJDCN() {

        let nodes = await this.forJD();

        console.log("Save in export:", nodes)

        if (nodes > 0) {
            let name = this.workflow_name + "_with_media";
            let graph = this.app.serializeGraph();
            let images = this.images;

            graph.workflow_images = images

            const jsonString = JSON.stringify(graph, null, 2);
            const blob = new Blob([jsonString], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');

            a.href = url;
            a.download = `${name}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);

            URL.revokeObjectURL(url);
        }

    }

}

let JDCN_LoadImageFObj = new JDCN_LoadImageF(app);
let JDCN_LoadImageFExt = {
    name: "ComfyUI-JDCN_LoadImageF",
    async setup() {
        let originalNodeAdded = app.graph.onNodeAdded ? app.graph.onNodeAdded.bind(app.graph) : null;
        let originalNodeRemoved = app.graph.onNodeRemoved ? app.graph.onNodeRemoved.bind(app.graph) : null;

        app.graph.onNodeAdded = function (node) {
            if (originalNodeAdded) originalNodeAdded(node);
            JDCN_LoadImageFObj.onNodeAdded(node);
        };

        app.graph.onNodeRemoved = function (node) {
            if (originalNodeRemoved) originalNodeRemoved(node);
            JDCN_LoadImageFObj.onNodeRemoved(node);
        };

    },
    async afterConfigureGraph() {
        console.log("JDCN Load Image Extension Loaded");
        JDCN_LoadImageFObj.registerNodes();
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
