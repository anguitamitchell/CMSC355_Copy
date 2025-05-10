//This controller "listens" for user responses.
//TODO: We need to figure out how to set the user input into a DTO, then convert to Model and add into database

package com.jydoc.deliverable3.Controller;
import com.jydoc.deliverable3.DTO.UserDTO;
import com.jydoc.deliverable3.Model.UserModel;
import com.jydoc.deliverable3.Repository.UserRepository;
import com.jydoc.deliverable3.Service.UserService;
import jakarta.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;


import java.time.LocalDate;




@Controller
public class indexController {

    private final UserRepository userRepository;
    private final UserService userService;

    public indexController(UserRepository userRepository) {
        this.userRepository = userRepository;
        this.userService = new UserService();
    }

    // This method maps to the root URL ("/")
    @GetMapping("/")
    public String index(Model model) {

        // Add the current date to the model
        model.addAttribute("currentDate", LocalDate.now());

        // Return the name of the Thymeleaf template ("index")
        return "index";
    }

    @GetMapping("/login")
    public String login(Model model) {
        if (!model.containsAttribute("userDTO")) {
            model.addAttribute("userDTO", new UserDTO());
        }
        return "login"; // Make sure the login page is returned
    }

    @PostMapping("/login")
    public String handleLogin(@Valid @ModelAttribute("userDTO") UserDTO userDTO, BindingResult result, Model model) {

        if (result.hasErrors()) {
            return "login";
        }

        boolean isAuthenticated = userService.authenticate(userDTO.getEmail(), userDTO.getPassword());

        if(!isAuthenticated) {
            model.addAttribute("error", "Invalid email or password");
            return "login"; // Return to the login page and show an error message
        }
        return "redirect:/";



    }

    @GetMapping("/register")
    public String showRegistrationForm(Model model) {
        model.addAttribute("user", new UserDTO());
        return "register";
    }

    @PostMapping("/register")
    public String registerUser(@Valid @ModelAttribute("user") UserDTO userDTO, BindingResult result, Model model) {
        //TODO: Implement registration system

        if (result.hasErrors()) {

            return "register"; // TODO: Implement register error to bring popup then refresh
        }
        else {
            UserModel user = new UserModel();
            user.setEmail(userDTO.getEmail());
            user.setPassword(userDTO.getPassword());
            user.setFirstName(userDTO.getFirstName()); //TODO: Transfer to Service package
            user.setLastName(userDTO.getLastName());
            userRepository.save(user);
            return "redirect:/";
        }




    }
}
