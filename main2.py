import glfw as glfw
import numpy
from OpenGL.GL import *
import OpenGL.GL.shaders

vertex_shader = """
    #version 410
    in vec4 position;

    void main()
    {
        gl_Position = position;
    }

    """

fragment_shader = """
    #version 410
    out vec4 frag_color; 
     void main()
     {
        frag_color = vec4(1.0f,0.0f,0.0f,1.0f);
     }
    """


def main():
    global fragment_shader
    global vertex_shader
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    window = glfw.create_window(800, 600, "Red triangle", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    triangle = [-0.5, -0.5, 0.0,
                0.5, -0.5, 0.0,
                0.0, 0.5, 0.0]

    triangle = numpy.array(triangle, dtype=numpy.float32)

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 36, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(position)

    glUseProgram(shader)

    glClearColor(1, 1, 1, 1)
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
