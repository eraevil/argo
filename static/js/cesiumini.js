let viewer;
let scene;
let camera;
let globe;
let canvas;
let ellipsoid;
let clock;
let baselayer;
let imagerylayer;
let selectedentity;
$(function () {
    let options = {
        animation:false,
        baseLayerPicker:false,
        fullscreenButton:false,
        vrButton:false,
        geocoder:true,
        homeButton:true,
        sceneModePicker:true,
        timeline:false,
        navigationHelpButton:false,
        navigationInstructionsInitiallyVisible:false,
        scene3DOnly:false,
        // sceneMode:Cesium.SceneMode.SCENE3D,
        sceneMode:Cesium.SceneMode.SCENE2D,
        terrainProvider: Cesium.createWorldTerrain({
            requestWaterMask: true,
            requestVertexNormals: true
        }),
    };

    Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhZGRmNmJkYy0zMWM1LTRlYzAtODY3OC1kMGFhZjhiZGJiMmQiLCJpZCI6OTI1NTEsImlhdCI6MTY1MTgwMjY0NH0.VJ5fmZb2_MsglH0aUsIUtrOkOHHgqk8ULOLJEJ_hSWs';
    viewer = new Cesium.Viewer('cesiumContainer',options);
    viewer.cesiumWidget.creditContainer.style.display = 'none';
    viewer.extend(Cesium.viewerDragDropMixin);
    viewer.imageryLayers.removeAll();

    // cesiumjs启动位置
    camera = viewer.camera;
    canvas = viewer.canvas;
    scene = viewer.scene;
    globe = scene.globe;
    ellipsoid = globe.ellipsoid;
    clock = viewer.clock;

    const home = Cesium.Rectangle.fromDegrees(73, 3, 135, 54);
    Cesium.Camera.DEFAULT_VIEW_RECTANGLE = home;
    // Cesium.Camera.DEFAULT_VIEW_RECTANGLE = Cesium.Rectangle.fromDegrees(70, -1, 140, 60); //默认矩形
    Cesium.Camera.DEFAULT_VIEW_FACTOR = 0.5;
    camera.flyHome(3);


    // 加载地图
    let url = 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer';
    let esri = new Cesium.ArcGisMapServerImageryProvider({url: url});
    viewer.imageryLayers.addImageryProvider(esri);

//    let wms = new Cesium.WebMapServiceImageryProvider({
//        url: "https://nationalmap.gov.au/proxy/http://geoserver.nationalmap.nicta.com.au/geotopo_250k/ows",
//        layers: "Hydrography:bores",
//        parameters: {
//            transparent: true,
//            format: "image/png",
//        }
//    });
//    viewer.imageryLayers.addImageryProvider(wms);
    // geosever图层加载
    let wms = new Cesium.WebMapServiceImageryProvider({
        url: 'http://127.0.0.1:8080/geoserver/argoproject/wms',
        layers: 'argoproject:argometa',
        parameters: {
            service: 'WMS',
            transparent: true,
            format: 'image/png',
        },
    });
   viewer.imageryLayers.addImageryProvider(wms);
//     let nclayer = new Cesium.WebMapServiceImageryProvider({
//         url: 'http://127.0.0.1:8080/geoserver/argoproject/wms',
//         layers: 'argoproject:boa202103temp5',//
//         enablePickFeatures: true,
// //        rectangle: Cesium.Rectangle.fromDegrees(96, 0, 153, 30),
//         parameters: {
//             service: 'WMS',
//             version: '1.1.0',
//             transparent: true,
//             format: 'image/png',
//             styles: 'argoproject:boa202103temp5',
//         }
//     });
//     viewer.imageryLayers.addImageryProvider(nclayer);

})

