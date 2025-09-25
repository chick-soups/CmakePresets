# Docs: https://developer.android.com/ndk/guides/cmake#android_native_api_level
ANDROID_NATIVE_API_LEVEL = 24
cmake_common_vars = {
    # Docs: https://source.android.com/docs/setup/about/build-numbers
    # Docs: https://developer.android.com/studio/publish/versioning
    'ANDROID_COMPILE_SDK_VERSION': 35,
    'ANDROID_TARGET_SDK_VERSION': 35,
    'ANDROID_MIN_SDK_VERSION': 24,
    'ANDROID_GRADLE_JAVA_VERSION': '21',
    # Docs: https://developer.android.com/studio/releases/gradle-plugin
    'ANDROID_GRADLE_PLUGIN_VERSION': '8.9.2',
    'GRADLE_VERSION': '8.11.1',
    'KOTLIN_PLUGIN_VERSION': '2.1.10',
    'ANDROID_STL':'c++_shared',
    'CMAKE_CXX_STANDARD': '17',
    'ZLIB_ROOT': 'D:/libraries/zlib/arm64-android',
    'JPEG_INCLUDE_DIR': 'D:/libraries/libjpeg-turbo/arm64-android/include',
    'JPEG_LIBRARY': 'D:/libraries/libjpeg-turbo/arm64-android/lib/libjpeg.so',
    'PNG_PNG_INCLUDE_DIR': 'D:/libraries/libpng/arm64-android/include',
    'PNG_LIBRARY': 'D:/libraries/libpng/arm64-android/lib/libpng16.so',
    'BUILD_JPEG':'OFF',
    'BUILD_PNG':'OFF',
    'WITH_TIFF':'OFF',
    'WITH_WEBP':'OFF',
    'WITH_OPENJPEG':'OFF',
    'WITH_OPENEXR':'OFF',
    'WITH_OPENEXR':'OFF',
    'WITH_OPENJPEG':'OFF',
    'WITH_JASPER':'OFF',
    'BUILD_SHARED_LIBS':'ON',
    'BUILD_ZLIB':'OFF',
    'BUILD_opencv_world': 'OFF',
    'BUILD_ANDROID_EXAMPLES':'OFF',
    'BUILD_ANDROID_PROJECTS':'ON',
    'BUILD_KOTLIN_EXTENSIONS':'ON',
    'BUILD_JAVA':'ON',
    'BUILD_FAT_JAVA_LIB':'OFF',
    'ENABLE_CCACHE':'ON',
    
}
ABIs = [
    ABI('3', 'arm64-v8a',   None, ndk_api_level=ANDROID_NATIVE_API_LEVEL, cmake_vars=cmake_common_vars),
]
