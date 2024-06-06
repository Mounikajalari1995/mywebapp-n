# Use a base image
FROM nginx:alpine

# Copy HTML files to the nginx html directory
COPY index.html /usr/share/nginx/html

# Expose port
EXPOSE 80

# Command to run the frontend
CMD ["nginx", "-g", "daemon off;"]
