//
//  ResultWindowController.h
//  RemoteDx
//
//  Created by David Cox on 9/10/17.
//
//

#ifndef ResultWindowController_h
#define ResultWindowController_h

#import <AppKit/AppKit.h>

#import <WebKit/WebView.h>

@interface ResultWindowController : NSWindowController {
    
    char*					myPointer;
    
    IBOutlet	WebView		*web;
}

- (void) loadContent: (NSString *) content;

@end


#endif /* ResultWindowController_h */
