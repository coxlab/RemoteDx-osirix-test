// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: mammogram_header.proto

// This CPP symbol can be defined to use imports that match up to the framework
// imports needed when using CocoaPods.
#if !defined(GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS)
 #define GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS 0
#endif

#if GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS
 #import <Protobuf/GPBProtocolBuffers_RuntimeSupport.h>
#else
 #import "GPBProtocolBuffers_RuntimeSupport.h"
#endif

 #import "MammogramHeader.pbobjc.h"
// @@protoc_insertion_point(imports)

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

#pragma mark - MammogramHeaderRoot

@implementation MammogramHeaderRoot

// No extensions in the file and no imports, so no need to generate
// +extensionRegistry.

@end

#pragma mark - MammogramHeaderRoot_FileDescriptor

static GPBFileDescriptor *MammogramHeaderRoot_FileDescriptor(void) {
  // This is called by +initialize so there is no need to worry
  // about thread safety of the singleton.
  static GPBFileDescriptor *descriptor = NULL;
  if (!descriptor) {
    GPB_DEBUG_CHECK_RUNTIME_VERSIONS();
    descriptor = [[GPBFileDescriptor alloc] initWithPackage:@""
                                                     syntax:GPBFileSyntaxProto2];
  }
  return descriptor;
}

#pragma mark - Enum ImageType

GPBEnumDescriptor *ImageType_EnumDescriptor(void) {
  static GPBEnumDescriptor *descriptor = NULL;
  if (!descriptor) {
    static const char *valueNames =
        "Uint8\000Uint16\000Float32\000Rgb\000Rgba\000";
    static const int32_t values[] = {
        ImageType_Uint8,
        ImageType_Uint16,
        ImageType_Float32,
        ImageType_Rgb,
        ImageType_Rgba,
    };
    GPBEnumDescriptor *worker =
        [GPBEnumDescriptor allocDescriptorForName:GPBNSStringifySymbol(ImageType)
                                       valueNames:valueNames
                                           values:values
                                            count:(uint32_t)(sizeof(values) / sizeof(int32_t))
                                     enumVerifier:ImageType_IsValidValue];
    if (!OSAtomicCompareAndSwapPtrBarrier(nil, worker, (void * volatile *)&descriptor)) {
      [worker release];
    }
  }
  return descriptor;
}

BOOL ImageType_IsValidValue(int32_t value__) {
  switch (value__) {
    case ImageType_Uint8:
    case ImageType_Uint16:
    case ImageType_Float32:
    case ImageType_Rgb:
    case ImageType_Rgba:
      return YES;
    default:
      return NO;
  }
}

#pragma mark - MammogramHeader

@implementation MammogramHeader

@dynamic hasImageId, imageId;
@dynamic hasWidth, width;
@dynamic hasHeight, height;
@dynamic hasImtype, imtype;

typedef struct MammogramHeader__storage_ {
  uint32_t _has_storage_[1];
  int32_t width;
  int32_t height;
  ImageType imtype;
  NSString *imageId;
} MammogramHeader__storage_;

// This method is threadsafe because it is initially called
// in +initialize for each subclass.
+ (GPBDescriptor *)descriptor {
  static GPBDescriptor *descriptor = nil;
  if (!descriptor) {
    static GPBMessageFieldDescription fields[] = {
      {
        .name = "imageId",
        .dataTypeSpecific.className = NULL,
        .number = MammogramHeader_FieldNumber_ImageId,
        .hasIndex = 0,
        .offset = (uint32_t)offsetof(MammogramHeader__storage_, imageId),
        .flags = GPBFieldRequired,
        .dataType = GPBDataTypeString,
      },
      {
        .name = "width",
        .dataTypeSpecific.className = NULL,
        .number = MammogramHeader_FieldNumber_Width,
        .hasIndex = 1,
        .offset = (uint32_t)offsetof(MammogramHeader__storage_, width),
        .flags = GPBFieldRequired,
        .dataType = GPBDataTypeInt32,
      },
      {
        .name = "height",
        .dataTypeSpecific.className = NULL,
        .number = MammogramHeader_FieldNumber_Height,
        .hasIndex = 2,
        .offset = (uint32_t)offsetof(MammogramHeader__storage_, height),
        .flags = GPBFieldRequired,
        .dataType = GPBDataTypeInt32,
      },
      {
        .name = "imtype",
        .dataTypeSpecific.enumDescFunc = ImageType_EnumDescriptor,
        .number = MammogramHeader_FieldNumber_Imtype,
        .hasIndex = 3,
        .offset = (uint32_t)offsetof(MammogramHeader__storage_, imtype),
        .flags = (GPBFieldFlags)(GPBFieldRequired | GPBFieldHasEnumDescriptor),
        .dataType = GPBDataTypeEnum,
      },
    };
    GPBDescriptor *localDescriptor =
        [GPBDescriptor allocDescriptorForClass:[MammogramHeader class]
                                     rootClass:[MammogramHeaderRoot class]
                                          file:MammogramHeaderRoot_FileDescriptor()
                                        fields:fields
                                    fieldCount:(uint32_t)(sizeof(fields) / sizeof(GPBMessageFieldDescription))
                                   storageSize:sizeof(MammogramHeader__storage_)
                                         flags:GPBDescriptorInitializationFlag_None];
    NSAssert(descriptor == nil, @"Startup recursed!");
    descriptor = localDescriptor;
  }
  return descriptor;
}

@end


#pragma clang diagnostic pop

// @@protoc_insertion_point(global_scope)
