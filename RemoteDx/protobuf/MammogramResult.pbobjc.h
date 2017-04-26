// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: mammogram_result.proto

// This CPP symbol can be defined to use imports that match up to the framework
// imports needed when using CocoaPods.
#if !defined(GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS)
 #define GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS 0
#endif

#if GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS
 #import <Protobuf/GPBProtocolBuffers.h>
#else
 #import "GPBProtocolBuffers.h"
#endif

#if GOOGLE_PROTOBUF_OBJC_VERSION < 30002
#error This file was generated by a newer version of protoc which is incompatible with your Protocol Buffer library sources.
#endif
#if 30002 < GOOGLE_PROTOBUF_OBJC_MIN_SUPPORTED_VERSION
#error This file was generated by an older version of protoc which is incompatible with your Protocol Buffer library sources.
#endif

// @@protoc_insertion_point(imports)

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

CF_EXTERN_C_BEGIN

NS_ASSUME_NONNULL_BEGIN

#pragma mark - Enum ResultImageType

typedef GPB_ENUM(ResultImageType) {
  ResultImageType_Uint8 = 0,
  ResultImageType_Uint16 = 1,
  ResultImageType_Float32 = 2,
  ResultImageType_Rgb = 3,
  ResultImageType_Rgba = 4,
};

GPBEnumDescriptor *ResultImageType_EnumDescriptor(void);

/**
 * Checks to see if the given value is defined by the enum or was not known at
 * the time this source was generated.
 **/
BOOL ResultImageType_IsValidValue(int32_t value);

#pragma mark - MammogramResultRoot

/**
 * Exposes the extension registry for this file.
 *
 * The base class provides:
 * @code
 *   + (GPBExtensionRegistry *)extensionRegistry;
 * @endcode
 * which is a @c GPBExtensionRegistry that includes all the extensions defined by
 * this file and all files that it depends on.
 **/
@interface MammogramResultRoot : GPBRootObject
@end

#pragma mark - MammogramResult

typedef GPB_ENUM(MammogramResult_FieldNumber) {
  MammogramResult_FieldNumber_ImageId = 1,
  MammogramResult_FieldNumber_Width = 2,
  MammogramResult_FieldNumber_Height = 3,
  MammogramResult_FieldNumber_Score = 4,
  MammogramResult_FieldNumber_Imtype = 5,
};

@interface MammogramResult : GPBMessage

@property(nonatomic, readwrite, copy, null_resettable) NSString *imageId;
/** Test to see if @c imageId has been set. */
@property(nonatomic, readwrite) BOOL hasImageId;

@property(nonatomic, readwrite) int32_t width;

@property(nonatomic, readwrite) BOOL hasWidth;
@property(nonatomic, readwrite) int32_t height;

@property(nonatomic, readwrite) BOOL hasHeight;
@property(nonatomic, readwrite) float score;

@property(nonatomic, readwrite) BOOL hasScore;
@property(nonatomic, readwrite) ResultImageType imtype;

@property(nonatomic, readwrite) BOOL hasImtype;
@end

NS_ASSUME_NONNULL_END

CF_EXTERN_C_END

#pragma clang diagnostic pop

// @@protoc_insertion_point(global_scope)
