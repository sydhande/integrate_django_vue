import http from "../http-common";

class RentDataService {
  getAll() {
    return http.get("/rentsites/");
  }
}

export default new RentDataService();