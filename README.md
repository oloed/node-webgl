# node-glfw

This is a port of WebGL for desktops: windows, linux, mac

It started as an extension of creationix/node-webgl and their great example com.creationix.minimason that you can find in examples/wavefront.js. However, it is now quite different and support different platform bindings, mainly GLFW instead of SDL.


## Dependencies

- node-glfw
which depends on GLEW and GLFW. See node-glfw for installation instructions.

- freeimage
freeimage is used to load/save a variety of image formats.


## Installation

`npm install` or `node-waf configure build`


## Usage

- `examples/`   contains examples from other the web.
- `test/`       contains lessons from www.learningwebgl.com and other tests.

simply type: node test/lesson02.js

Enjoy!


## Limitations

WebGL is based on OpenGL ES, a subset of OpenGL made for embedded systems.  Because this module wraps OpenGL, it is possible to do things that may not work on web browsers.  Please refer to [Khronos's wiki][wiki] to learn about the differences.

[wiki]: http://www.khronos.org/webgl/wiki_1_15/index.php/WebGL_and_OpenGL_Differences

- **Shaders**
    
    Remember to add this on top of your fragment shaders:
    
        #ifdef GL_ES
        precision highp float;
        #endif


- **Loading External Scripts**
    
    If your code uses external libraries, you can load them like this. No code change to external scripts ;-)
    
        fs=require('fs');
        eval(fs.readFileSync(__dirname+ '/glMatrix-0.9.5.min.js','utf8'));


- **Framerate**
    
    `requestAnimationFrame(callback [, delay = 16])` works the same as in the browser.
    
    A delay, if specified, is the delay in milliseconds between animation frames.  For example, a delay of 16 will come out to 62 frames per second (`1000 / 16`) at best.  If unspecified, delays are 16 milliseconds.  If you specify a delay of 0 (zero), the fastest possible framerate on your machine is used.
